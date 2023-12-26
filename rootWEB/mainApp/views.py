from django.shortcuts import render
from django.db import connections, connection
from django.http import JsonResponse, HttpResponse
from django.views import View
import pandas as pd
import numpy as np
import joblib
from joblib import load
import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from .models import UserModel, EmptyRoomData
from .models import LikeModel
from django.shortcuts import get_object_or_404
import json

def index(request) :
    print('debug >>> client path, mainApp/index, render = index')
    return render(request, 'main/index.html')

def map(request) :
    return render(request, 'main/map.html')

# Create your views here.
def sign(request):
    if request.method == 'POST':
        email    = request.POST.get('email', None)
        password = request.POST.get('password', None)
        username = request.POST.get('username', None)
        try:
            me = UserModel.objects.get(email=email)

            if me.password == password:
                request.session['user'] = me.username
                return redirect('/')
            else:
                return redirect('/sign')
        except UserModel.DoesNotExist:
            return redirect('/sign')

    elif request.method == 'GET':
        return render(request, 'main/sign.html')

def signup(request):
    if request.method == "GET":
        return render(request, 'main/signup.html')
    elif request.method == 'POST':
        username  = request.POST.get('username', None)
        email     = request.POST.get('email', None)
        password  = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        phone     = request.POST.get('phone', None)

        if password != password2:
            return render(request, 'main/signup.html')
        else:
            exist_user = UserModel.objects.filter(email=email)
            if exist_user:
                return render(request, 'main/signup.html')
            else:
                new_user = UserModel()
                new_user.email    = email
                new_user.username = username
                new_user.password = password
                new_user.phone    = phone
                new_user.save()
                return redirect('/sign')


def logout(request):
    # 세션 제거
    if 'user' in request.session:
        del request.session['user']

    return redirect('/')

def busan(request):
    print('debug >>> client path, mainApp/busan, render = busan')
    return render(request,'main/busan.html')

def analysis_lease(request):
    with connection.cursor() as cursor:
        final_dict = {}
        guLst = []
        yearLst = []
        leaseLst = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM lease_trend_final")

            # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            gulst = [i['index'] for i in data]
            # year = [i for i in range(2014, 2023)]
            datas = []
            for i in data:
                for gu in gulst:
                    if i['index'] == gu:
                        temp = [j for j in i.values()][1:]
                        temp = [int(i) for i in temp]
                        datas.append({'name': gu, 'data' : temp })

        # JSON 형식으로 응답
        return JsonResponse({'data': datas}, safe=False)

def kakaomap(request):
    return render(request, 'main/kakaomap.html')

def analysis_zipgac(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM zipgac_number")

        # 쿼리 결과를 필요한 형식으로 가공
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # 데이터를 Highcharts에서 사용할 수 있는 형태로 가공
        gu_list = [entry['gu'] for entry in data]
        number_values = [int(entry['number']) for entry in data]
        map = []
        for idx,e in enumerate(gu_list):
            map.append([e,number_values[idx]])

        processed_data = [{'name': '집객시설 수', 'data': number_values,'map':map,'title':'부산시 집객 시설 분포도','text': '집객시설 수'}]

        # JSON 형식으로 응답
        return JsonResponse({'data': processed_data, 'gu': gu_list}, safe=False)


def analysis_pop_density(request):
    final_dict = {}
    guLst = []
    popuLst = []
    gu_list = ['강서구', '중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '강서구', '연제구', '수영구',
               '사상구']
    with connection.cursor() as cursor:
        cursor.execute("SELECT gu, popu_density FROM population_info")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        map_data = {}
        map_data['map'] = []
        for i in data:
            map_data['map'].append([i['gu'],i['popu_density']])
        map_data['title'] = '부산시 인구밀도 분포도'
        map_data['text'] = '인구밀도'
        for i in range(len(data)):
            if data[i]['gu'] in gu_list:
                guLst.append(data[i]['gu'])
                popuLst.append(data[i]['popu_density'])
            else:
                guLst.append(data[i]['gu'])
                popuLst.append(data[i]['popu_density'])
        final_dict['gu'] = guLst
        final_dict['popu_density'] = popuLst
        data = final_dict


    return JsonResponse({'data': data, 'map':map_data}, safe=False)


def analysis_pop_cnt(request):
    final_dict2 = {}
    guLst2 = []
    popuLst2 = []
    gu_list = ['강서구', '중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '강서구', '연제구', '수영구',
               '사상구']
    with connection.cursor() as cursor:
        cursor.execute("SELECT gu, popu_cnt FROM population_info")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        map_data= {}
        map_data['map'] = []
        for i in data:
            map_data['map'].append([i['gu'],i['popu_cnt']])
        map_data['title'] = '부산시 인구수 분포도'
        map_data['text'] = '인구수'
        for i in range(len(data)):
            if data[i]['gu'] in gu_list:
                guLst2.append(data[i]['gu'])
                popuLst2.append(data[i]['popu_cnt'])
            else:
                guLst2.append(data[i]['gu'])
                popuLst2.append(data[i]['popu_cnt'])
        final_dict2['gu'] = guLst2
        final_dict2['popu_cnt'] = popuLst2
        data = final_dict2
    return JsonResponse({'data': data,'map':map_data}, safe=False)



def analysis_service_cnt(request):
    query = (
        "SELECT gu, avg(service_population_per_store) FROM store_density group by gu having avg(service_population_per_store)")
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return JsonResponse({'data': data})


def analysis_store_density(request):
    query = ("SELECT gu, avg(density) FROM store_density group by gu having avg(density)")
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        map_data = {}
        map_data['map'] = []
        for i in data:
            print(i)
            map_data['map'].append([i['gu'], int(i['avg(density)'])])
        map_data['title'] = '부산시 점포 밀도 분포도'
        map_data['text'] = '점포 밀도'
    return JsonResponse({'data': data,'map':map_data})

from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

def get_center_coordinates(gu):
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

    return gu_coordinates.get(gu, (0, 0))

def hospital_json(request):
    print('debug >>>> ')
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM hospital_20230927")
            locations = cursor.fetchall()

        data = [
            {
                "hospital": location[0],
                "lat": location[1],
                "lng": location[2],
            }
            for location in locations
        ]

        return JsonResponse(data, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def hospital(request):
    return render(request,'main/hospital.html')

def school_json(request):
    try:
        # GET 요청에서 'gu' 매개변수의 값을 추출합니다.
        gu = request.GET.get('gu', None)

        # 'gu'를 사용하여 중심 좌표를 가져옵니다.
        center_latitude, center_longitude = get_center_coordinates(gu)

        # 데이터베이스 커서를 사용하여 SQL 쿼리를 실행합니다.
        with connection.cursor() as cursor:
            # 'gu'에 따라 필터링된 쿼리를 실행합니다.
            cursor.execute(
                "SELECT gu, name, address, category, type, est, lat, lng FROM school_lat_lng where gu=%s",[gu])
            # 실행된 쿼리에서 모든 결과를 가져옵니다.
            locations = cursor.fetchall()

        # 가져온 데이터를 JSON 직렬화 가능한 형식으로 처리합니다.
        data = [
            {
                "gu": location[0],
                "name": location[1],
                "address": location[2],
                "category": location[3],
                "type": location[4],
                "est": location[5],
                "lat": location[6],
                "lng": location[7],
            }
            for location in locations
        ]

        # 처리된 데이터와 중심 좌표를 포함한 JSON 응답을 반환합니다.
        return JsonResponse({"data": data, "center_latitude": center_latitude, "center_longitude": center_longitude},
                            safe=False)

    except Exception as e:
        # 예외가 발생하면 에러 메시지를 포함한 500 상태의 JSON 응답을 반환합니다.
        return JsonResponse({"error": str(e)}, status=500)


def school(request):
    return render(request, 'main/school.html')

from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection



from django.http import JsonResponse
from django.db import connection

def subwayloc_json(request):
    try:
        # GET 요청에서 'gu' 매개변수의 값을 추출합니다.
        gu = request.GET.get('gu', None)

        # 'gu'를 사용하여 중심 좌표를 가져옵니다.
        center_latitude, center_longitude = get_center_coordinates(gu)

        # 데이터베이스 커서를 사용하여 SQL 쿼리를 실행합니다.
        with connection.cursor() as cursor:
            # 'gu'에 따라 필터링된 쿼리를 실행합니다.
            cursor.execute("SELECT l.gu, l.sang_name, l.subway_name, l.lat, l.lng, round(p.sum, 1) FROM subway_lat_lng l INNER JOIN subway_session_population p ON l.subway_name = p.station WHERE l.gu = %s", [gu])
            # 실행된 쿼리에서 모든 결과를 가져옵니다.
            locations = cursor.fetchall()

        # 가져온 데이터를 JSON 직렬화 가능한 형식으로 처리합니다.
        data = [
            {
                "gu": location[0],
                "sang_name": location[1],
                "subway_name": location[2],
                "lat": location[3],
                "lng": location[4],
                "sum": location[5],
            }
            for location in locations
        ]

        # 처리된 데이터와 중심 좌표를 포함한 JSON 응답을 반환합니다.
        return JsonResponse({"data": data, "center_latitude": center_latitude, "center_longitude": center_longitude}, safe=False)

    except Exception as e:
        # 예외가 발생하면 에러 메시지를 포함한 500 상태의 JSON 응답을 반환합니다.
        return JsonResponse({"error": str(e)}, status=500)

def subwayloc(request):
    return render(request, 'main/subwayloc.html')


from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.db.models import Count
from django.core.serializers import serialize

def busstop_json(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    bstopnm,
                    gpsx,
                    gpsy,
                FROM
                    busstop
            """)
            locations = cursor.fetchall()

        data = [
            {
                "bstopnm": location[0],
                "gpsx": location[1],
                "gpsy": location[2],
                "count": location[3],
            }
            for location in locations
        ]
        return JsonResponse(data, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def busstop(request):
    return render(request, 'main/busstop_clustered.html')

def predict(request) :
    return render(request, 'main/predict.html')

def predict_model(request) :
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # 입력 데이터 예시: {'보증금_y': 1000, '상가구분': 3, '임대(계약)면적': 89.84, '전용면적': 63.20, '해당층': 2, '총층': 3}

            model_path = os.path.join(os.path.dirname(__file__), 'static', 'model_predict', 'predict_model.pkl')
            predict_model = joblib.load(model_path)

            input_data = [float(data['보증금_y']), float(data['상가구분']), float(data['임대(계약)면적']), float(data['전용면적']), float(data['해당층']), float(data['총층'])]

            prediction = int(predict_model.predict([input_data])[0])

            response_data = {'prediction': prediction}
            return JsonResponse(response_data)

        except Exception as e:
            response_data = {'error': str(e)}
            return JsonResponse(response_data, status=400)

    else:
        response_data = {'error': 'Only POST requests are allowed.'}
        return JsonResponse(response_data, status=400)

def mypage(request):
    return render(request,'main/mypage.html')

def mypage_view(request):
    if 'user' in request.session:
        user_id = request.session['user']
        user = UserModel.objects.get(pk=user_id)
        print(user_id)
        return render(request, 'main/mypage.html', {'user': user})
    else:
        print("Debug: User does not exist in the view.")
        return redirect('/login')
