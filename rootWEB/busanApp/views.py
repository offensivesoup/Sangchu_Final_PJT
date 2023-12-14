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



def index(request):
    print('debug >>> busanApp/index ')
    final_dict = {}
    guLst = []
    categoryLst = []
    densityLst = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT gu, category, density FROM store_density")
        # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for i in range(len(data)):
            if data[i]['gu'] == '강서구':
                guLst.append(data[i]['gu'])
                categoryLst.append(data[i]['category'])
                densityLst.append(data[i]['density'])
        final_dict['gu'] = guLst
        final_dict['category'] = categoryLst
        final_dict['density'] = densityLst
        data = final_dict
        ctx = {'data': data}

    return render(request, 'busan/index.html',ctx)

def json_store_density_view(request) :
    final_dict = {}
    guLst = []
    categoryLst = []
    densityLst = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT gu, category, density FROM store_density")
        # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for i in range(len(data)):
            if data[i]['gu'] == '강서구':
                guLst.append(data[i]['gu'])
                categoryLst.append(data[i]['category'])
                densityLst.append(data[i]['density'])
        final_dict['gu'] = guLst
        final_dict['category'] = categoryLst
        final_dict['density'] = densityLst
        data = final_dict
    # JSON 형식으로 응답
        return JsonResponse({'data': data}, safe=False)

# 서비스 인구
def json_service_density_view(request):
    final_dict = {}
    guLst = []
    categoryLst = []
    serviceLst = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT gu, category, service_population_per_store FROM store_density")
        # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for i in range(len(data)):
            if data[i]['gu'] == '강서구':
                guLst.append(data[i]['gu'])
                categoryLst.append(data[i]['category'])
                serviceLst.append(data[i]['service_population_per_store'])
        final_dict['gu'] = guLst
        final_dict['category'] = categoryLst
        final_dict['service'] = serviceLst
        data = final_dict
        # JSON 형식으로 응답
        return JsonResponse({'data': data}, safe=False)

# 임대료 추세
def json_lease_trend_view(request) :
    final_dict = {}
    guLst = []
    yearLst = []
    leaseLst = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM lease_trend_final")

        # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for i in range(len(data)):
            if data[i]['index'] == '수영구':
                guLst.append(data[i]['index'])
                yearLst = [i for i in data[i].keys()][1:]
                leaseLst = [m for m in data[i].values()][1:]
        final_dict['gu'] = guLst
        final_dict['year'] = yearLst
        final_dict['lease'] = leaseLst
        data = final_dict
        print(final_dict)
    # JSON 형식으로 응답
    return JsonResponse({'data': data}, safe=False)

# 집객시설
def json_zipgac_number_view(request) :
    final_dict = {}
    guLst = []
    numLst = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT gu, number FROM zipgac_number")
        # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for i in range(len(data)):
            if data[i]['gu'] == '강서구':
                guLst.append(data[i]['gu'])
                numLst.append(data[i]['number'])
        final_dict['gu'] = guLst
        final_dict['number'] = numLst
        data = final_dict

    # JSON 형식으로 응답
    return JsonResponse({'data': data}, safe=False)

# 인구밀도
def json_population_density_view(request) :
    final_dict = {}
    guLst = []
    popuLst = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT gu, popu_density FROM population_info")
        # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for i in range(len(data)):
            if data[i]['gu'] == '강서구':
                guLst.append(data[i]['gu'])
                popuLst.append(data[i]['popu_density'])
        final_dict['gu'] = guLst
        final_dict['popu_density'] = popuLst
        data = final_dict
    # JSON 형식으로 응답
    return JsonResponse({'data': data}, safe=False)

# 아래는 구별 인구밀도에 대한 전체 정보를 가져오는 코드입니다.(진우)
def json_population_density_view_all(request):
    final_dict = {}
    guLst = []
    popuLst = []
    gu_list = ['강서구', '중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '강서구', '연제구', '수영구', '사상구']
    with connection.cursor() as cursor:
        cursor.execute("SELECT gu, popu_density FROM population_info")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for i in range(len(data)):
            if data[i]['gu'] in gu_list:
                guLst.append(data[i]['gu'])
                popuLst.append(data[i]['popu_density'])
            else:
                guLst.append(data[i]['gu'])
                popuLst.append(data[i]['popu_density'])
        final_dict['gu'] = guLst
        final_dict['popu_density'] = popuLst

        chart_data = {
            'chart': {
                'type': 'bar'
            },
            'title': {
                'text': '구별 단위면적 당 인구 수(인구밀도)'
            },
            'xAxis': {
                'categories': final_dict['gu'],  # Corrected this line
                'title': {
                    'text': '구 명'
                }
            },
            'yAxis': {
                'title': {
                    'text': '단위면적 당 인구 수'
                }
            },
            'series': [{
                'name': '단위면적 당 인구 수',
                'data': final_dict['popu_density']
            }]
        }
        return render(request, 'busan/population_density_chart.html', {'chart_data': chart_data})

def json_population_cnt_view(request) :
    final_dict = {}
    guLst = []
    cntLst = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT gu, popu_cnt FROM population_info")
        # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for i in range(len(data)):
            if data[i]['gu'] == '강서구':
                guLst.append(data[i]['gu'])
                cntLst.append(data[i]['popu_cnt'])
        final_dict['gu'] = guLst
        final_dict['popu_cnt'] = cntLst
        data = final_dict
    # JSON 형식으로 응답
    return JsonResponse({'data': data}, safe=False)

def predict_model_view(request):
    model_path = os.path.join(os.path.dirname(__file__), 'static', 'model_1', 'model_1.joblib')
    loaded_model = load(model_path)

    if request.method == 'POST':
        user_input = request.POST

        feature1 = float(user_input['feature1'])
        feature2 = float(user_input['feature2'])
        feature3 = float(user_input['feature3'])
        feature4 = float(user_input['feature4'])

        input_data = [[feature1, feature2, feature3, feature4]]
        predictions = loaded_model.predict(input_data)
        if predictions <= 0 or predictions >1000:
            predictions = "제공되지 않는 정보입니다."

        return render(request, 'busan/prediction_template.html', {'predictions': predictions})

    else:
        return render(request, 'busan/input_form.html')

# views.py
from django.shortcuts import render
from django.db import connection
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import os

def cosine_similarity_view(request, index):
    # 모델 로드
    model_path = os.path.join(os.path.dirname(__file__), 'static', 'model_cosine', 'cosine_model.pkl')
    loaded_model = joblib.load(model_path)

    # item_id에 해당하는 공실 정보를 데이터베이스에서 가져오기
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT address, deposit, monthly, maintenance_cost, `when`, division, lease_area, my_area, my_floor, total_floor
            FROM empty_room_data
            WHERE `index` = %s
        """, [index])
        row = cursor.fetchone()

    if row is None:
        return render(request, 'not_found.html')  # 해당 아이템이 없을 경우 not_found.html로 이동

    # 가져온 공실 정보를 가지고 유사한 아이템 추천
    input_item = f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]}"

    # 이미 계산된 코사인 유사도 가져오기
    similarities = loaded_model  # 적절한 변수나 메서드를 사용하여 가져와야 함

    current_page_index = index # 여기에 현재 페이지의 인덱스를 설정하세요.

    # 현재 페이지의 유사도를 기준으로 정렬
    sorted_similar_items = sorted(enumerate(similarities[current_page_index]), key=lambda x: x[1], reverse=True)

    # 상위 10개 아이템의 인덱스 추출
    top_10_similar_items = [index for index, _ in sorted_similar_items[1:11]]

    context = {
        'index' : index,
        'input_item': input_item,
        'recommended_items': top_10_similar_items,
    }

    return render(request, 'busan/cosine_sim.html', context)

## 구별 상세페이지로 이동시킬 것.

# def json_rent_mean_view(request) :
#     final_dict = {}
#     guLst = []
#     areaLst = []
#     yearLst = []
#     avgLst = []
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM rent_mean")
#         # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
#         columns = [col[0] for col in cursor.description]
#         data = [dict(zip(columns, row)) for row in cursor.fetchall()]
#         for i in range(len(data)):
#             if data[i]['gu'] == '부산광역시 강서구':
#                 guLst.append(data[i]['gu'])
#                 yearLst.append(data[i]['year'])
#                 areaLst.append(data[i]['area'])
#                 avgLst.append(data[i]['avg'])
#         final_dict['gu'] = guLst
#         final_dict['year'] = yearLst
#         final_dict['area'] = areaLst
#         final_dict['avg'] = avgLst
#     # JSON 형식으로 응답
#     return JsonResponse({'data': data}, safe=False)
