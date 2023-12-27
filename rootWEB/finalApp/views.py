from datetime import datetime, timedelta
from django.shortcuts import render
from django.db import connections, connection
from django.http import JsonResponse, HttpResponse
from django.views import View
import pandas as pd
import numpy as np
import joblib
from joblib import load
import os
import pandas as pd
from django.contrib.staticfiles import finders
import json
from django.db import transaction


# Create your views here.
def list(request,region_name):
    region_name = region_name
    print('debug >>> client path, finalApp/list, render = list')
    return render(request,'final/list.html',{'region_name':region_name})

def detail(request, region_name,maemul_id):
    print('debug >>> region_name: ', region_name)
    print('debug >>> maemul_id: ',maemul_id)
    print('debug >>> client path, finalApp/detail, render = detail')
    sql_query = "SELECT * FROM empty_room_data WHERE address = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql_query, (region_name,))
        result = cursor.fetchall()
        map_data = {}
        for row in result:
            if row[16] == maemul_id:
                map_data['map'] = {'index': row[16], 'deposit': row[0], 'month': row[1], 'criteria': row[2],
                        'lat': row[3], 'lng': row[4], 'address': row[5], 'when': row[6], 'area': row[7],
                        'my_area': row[8],
                        'my_floor': row[9], 'total_floor': row[10], 'now': row[11], 'recommend': row[12],
                        'parking': row[13], 'usage': row[14], 'direction': row[15]}
                break


    return render(request, 'final/detail.html', {'region_name' : region_name, 'maemul_id' : maemul_id,'map':map_data['map']})


def get_list(request,region_name):
    region_name = region_name
    page = request.GET.get('page', 1)
    items_per_page = 10
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    sql_query = "SELECT * FROM empty_room_data WHERE address = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql_query,(region_name,))
        result = cursor.fetchall()
        data = []
        for row in result:
            name = {'index':row[16],'address': row[5],'deposit':row[0],'month':row[1],'criteria':row[2],'lat':row[3],'lng':row[4],'area':row[7],'my_area':row[8],
                    'my_floor':row[9],'total_floor':row[10]}
            data.append(name)
        data = data[start_index:end_index]

        # # 쿼리 결과를 필요한 형식으로 가공
        # columns = [col[0] for col in cursor.description]
        # print(columns)
        # data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        # data = {'gu':'기장군','value':7}
    return JsonResponse({'data': data})



def get_detail(request,region_name,maemul_id):
    region_name = region_name
    maemul_id = maemul_id
    sql_query = "SELECT * FROM empty_room_data WHERE address = %s"

    with connection.cursor() as cursor:
        cursor.execute(sql_query, (region_name,))
        result = cursor.fetchall()
        data = []
        for row in result:
            name = {'index': row[16], 'deposit': row[0], 'month': row[1], 'criteria': row[2],
                    'lat': row[3], 'lng': row[4], 'address': row[5], 'when' : row[6], 'area': row[7], 'my_area': row[8],
                    'my_floor': row[9], 'total_floor': row[10], 'now' : row[11], 'recommend' : row[12],
                    'parking' : row[13], 'usage' : row[14], 'direction' : row[15]}
            if name['index'] == maemul_id:
                data.append(name)
            else:
                pass

    return JsonResponse({'data' : data})

## 추천 모델 올리기
def cosine_similarity_view(request, region_name, maemul_id):
    region_name = region_name
    maemul_id = maemul_id
    recommendation_list = []

    # 모델 로드
    model_path   = os.path.join(os.path.dirname(__file__), 'static', 'model_cosine', 'cosine_model.pkl')
    loaded_model = joblib.load(model_path)

    # item_id에 해당하는 공실 정보를 데이터베이스에서 가져오기
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM empty_room_data  WHERE `index` = %s""", [maemul_id])
        row = cursor.fetchone()
    # 사용자가 선택한 매물의 월세, 보증금 가져오기
    input_month = row[1]
    input_deposit = row[0]
    if row:
        recommendation_id = loaded_model.loc[loaded_model.loc[maemul_id]<1, maemul_id].drop_duplicates().nlargest(1000)
        with connection.cursor() as cursor:
            for i in range(len(recommendation_id)):
                index_value = recommendation_id.index[i]
                cursor.execute("""
                    SELECT * FROM empty_room_data 
                    WHERE `index` = %s """, [index_value])
                recommendation_row = cursor.fetchone()

                data = {'index': recommendation_row[16], 'deposit': recommendation_row[0], 'month': recommendation_row[1], 'criteria': recommendation_row[2],
                        'lat': recommendation_row[3], 'lng': recommendation_row[4], 'address': recommendation_row[5], 'when': recommendation_row[6], 'area': recommendation_row[7],
                        'my_area': recommendation_row[8],
                        'my_floor': recommendation_row[9], 'total_floor': recommendation_row[10], 'now': recommendation_row[11], 'recommend': recommendation_row[12],
                        'parking': recommendation_row[13], 'usage': recommendation_row[14], 'direction': recommendation_row[15]}

                if data['month'] < input_month:
                    recommendation_list.append(data)
                    if len(recommendation_list) > 4:
                        break
                else:
                    pass

        context = {
            'index': maemul_id,
            'recommendation': recommendation_list
        }
    else:
        context = {
            'index': maemul_id,
            'recommendation': None  # 추천할 데이터가 없는 경우 None으로 설정하거나 다른 처리 방식 선택
        }

    return JsonResponse({'data': context})

# def predict_model(request) :
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#
#             # 입력 데이터 예시: {'보증금_y': 1000, '상가구분': 3, '임대(계약)면적': 89.84, '전용면적': 63.20, '해당층': 2, '총층': 3}
#
#             model_path = os.path.join(os.path.dirname(__file__), 'static', 'model_predict', 'predict_model.pkl')
#             predict_model = joblib.load(model_path)
#
#             input_data = [data['보증금_y'], data['상가구분'], data['임대(계약)면적'], data['전용면적'], data['해당층'], data['총층']]
#             prediction = predict_model.predict([input_data])[0]
#
#             response_data = {'prediction': prediction}
#             return JsonResponse(response_data)
#
#         except Exception as e:
#             response_data = {'error': str(e)}
#             return JsonResponse(response_data, status=400)
#
#     else:
#         response_data = {'error': 'Only POST requests are allowed.'}
#         return JsonResponse(response_data, status=400)

from django.db import transaction


def detail_view(request, region_name, maemul_id):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT views FROM empty_room_data WHERE address = %s AND `index` = %s""",
                       [region_name, maemul_id])
        row = cursor.fetchone()

        if row is not None:
            current_views = row[0]
            # 트랜잭션 시작
            with transaction.atomic():
                cursor.execute("""UPDATE empty_room_data SET views = %s WHERE address = %s AND `index` = %s""",
                               [current_views + 1, region_name, maemul_id])
            new_views = current_views + 1
        else:
            new_views = None

        data = {'views': new_views}

    print(new_views)
    return JsonResponse(data)

def get_center_coordinates(region_name):
    gu_coordinates = {
        "기장군": (35.244394201041416, 129.2227421459612),
        "해운대구": (35.162995101348564, 129.16356675415742),
        "수영구": (35.145458076325326, 129.11307922758124),
        "남구": (35.136262710025456, 129.08468141230728),
        "연제구": (35.176129771565535, 129.079712017898),
        "동구": (35.129161209712215, 129.04558174709652),
        "중구": (35.10621258919303, 129.03247914653906),
        "서구": (35.09784717231878, 129.0242833944746),
        "영도구": (35.090989265185435, 129.06778927857764),
        "부산진구": (35.162697533668855, 129.05307148933218),
        "동래구": (35.196701579922234, 129.09391527580505),
        "금정구": (35.24278952025912, 129.09242514119632),
        "북구": (35.196830935641835, 128.99036558066425),
        "사상구": (35.15288084181415, 128.99035858685488),
        "사하구": (35.104261135161906, 128.97500193638786),
        "강서구": (35.21179065375177, 128.98045854324366),
    }

    return gu_coordinates.get(region_name, (0, 0))
    print(f"Region: {region_name}, Coordinates: {result}")
    return result

def gongsilmap(request, region_name):
    try:
        # 'gu'를 사용하여 중심 좌표를 가져옵니다.
        center_latitude, center_longitude = get_center_coordinates(region_name)

        # 데이터베이스 커서를 사용하여 SQL 쿼리를 실행합니다.
        with connection.cursor() as cursor:
            # 'gu'에 따라 필터링된 쿼리를 실행합니다.
            cursor.execute(
                "SELECT index, address, lat, lng, deposit, month FROM empty_room_data where address=%s",[region_name])
            # 실행된 쿼리에서 모든 결과를 가져옵니다.
            locations = cursor.fetchall()

        # 가져온 데이터를 JSON 직렬화 가능한 형식으로 처리합니다.
        data = [
            {
                "index": location[0],
                "address": location[1],
                "lat": location[2],
                "lng": location[3],
                "deposit": location[4],
                "month": location[5]
            }
            for location in locations
        ]

        print("JSON Result:", data)

        # 처리된 데이터와 중심 좌표를 포함한 JSON 응답을 반환합니다.
        return JsonResponse({"data": data, "center_latitude": center_latitude, "center_longitude": center_longitude},
                            safe=False)

    except Exception as e:
        # 예외가 발생하면 에러 메시지를 포함한 500 상태의 JSON 응답을 반환합니다.
        return JsonResponse({"error": str(e)}, status=500)
