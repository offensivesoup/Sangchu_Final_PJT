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
# def json_zipgac_number_view(request) :
#     final_dict = {}
#     guLst = []
#     numLst = []
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT gu, number FROM zipgac_number")
#         # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
#         columns = [col[0] for col in cursor.description]
#         data = [dict(zip(columns, row)) for row in cursor.fetchall()]
#         for i in range(len(data)):
#             if data[i]['gu'] == '강서구':
#                 guLst.append(data[i]['gu'])
#                 numLst.append(data[i]['number'])
#         final_dict['gu'] = guLst
#         final_dict['number'] = numLst
#         data = final_dict
#
#     # JSON 형식으로 응답
#     return JsonResponse({'data': data}, safe=False)

def json_zipgac_number_view(request):
    final_dict = {}
    gu_list = []
    number_list = []

    with connection.cursor() as cursor:
        cursor.execute("SELECT gu, number FROM zipgac_number")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        for entry in data:
            gu_list.append(entry['gu'])
            number_list.append(entry['number'])

    final_dict['gu'] = gu_list
    final_dict['number'] = number_list

    return JsonResponse({'data': final_dict}, safe=False)

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
        data = final_dict
    return JsonResponse({'data': data}, safe=False)

def population_density(request):
    return render(request, 'busan/population_density_chart.html')

def population_cnt_view(request):
    final_dict2 = {}
    guLst2 = []
    popuLst2 = []
    gu_list = ['강서구', '중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '강서구', '연제구', '수영구', '사상구']
    with connection.cursor() as cursor:
        cursor.execute("SELECT gu, popu_cnt FROM population_info")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
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
    return JsonResponse({'data': data}, safe=False)

def population_cnt(request):
    return render(request, 'busan/json_population_cnt_view.html')

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


# def get_lease_trend_data(request):
#     # HeidiSQL로 연결된 상태에서 실제 데이터베이스 테이블과 매칭되는 쿼리 작성
#     query = "SELECT * FROM lease_trend_final"
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         columns = [col[0] for col in cursor.description]
#         data = dict(zip(columns, zip(*cursor.fetchall())))
#
#     return JsonResponse(data)
#
# def lease_trend(request):
#     return render(request, 'busan/lease_trend.html')

from django.http import JsonResponse

def service_population_json(request):
    query = ("SELECT gu, avg(service_population_per_store) FROM store_density group by gu having avg(service_population_per_store)")
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return JsonResponse({'data': data})

def service_population(request):
    return render(request, 'busan/service_population.html')

def store_density_json(request):
    query = ("SELECT gu, avg(density) FROM store_density group by gu having avg(density)")
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return JsonResponse({'data': data})

def store_density(request):
    return render(request, 'busan/store_density.html')




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

def analysis_zipgac_number(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM zipgac_number")

        # 쿼리 결과를 필요한 형식으로 가공
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # 데이터를 Highcharts에서 사용할 수 있는 형태로 가공
        gu_list = [entry['gu'] for entry in data]
        number_values = [int(entry['number']) for entry in data]

        processed_data = [{'name': '집객시설 수', 'data': number_values}]

        # JSON 형식으로 응답
        return JsonResponse({'data': processed_data, 'gu': gu_list}, safe=False)

def json_zipgac_number_view(request) :
    return render(request, "busan/zipgac_number_view.html")