from django.shortcuts import render
from django.db import connections, connection
from django.http import JsonResponse, HttpResponse
from django.views import View
import pandas as pd
import numpy as np
import joblib
from joblib import load
import os



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
    aLst = []
    bLst = []
    cLst = []
    dLst = []
    eLst = []
    fLst = []
    gLst = []
    hLst = []
    iLst = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM lease_trend_final")

        # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for i in range(len(data)):
            if data[i]['index'] == '수영구':
                guLst.append(data[i]['index'])
                aLst.append(data[i]['2014'])
                bLst.append(data[i]['2015'])
                cLst.append(data[i]['2016'])
                dLst.append(data[i]['2017'])
                eLst.append(data[i]['2018'])
                fLst.append(data[i]['2019'])
                gLst.append(data[i]['2020'])
                hLst.append(data[i]['2021'])
                iLst.append(data[i]['2022'])
        final_dict['gu'] = guLst
        final_dict['2014'] = aLst
        final_dict['2015'] = bLst
        final_dict['2016'] = cLst
        final_dict['2017'] = dLst
        final_dict['2018'] = eLst
        final_dict['2019'] = fLst
        final_dict['2020'] = gLst
        final_dict['2021'] = hLst
        final_dict['2022'] = iLst
        data = final_dict
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

# 모델 로드
model_path = os.path.join(os.path.dirname(__file__), 'static', 'model_cosine', 'cosine_model.joblib')
loaded_model = joblib.load(model_path)

def cosine_similarity_maemul(input_item, model):
    # TF-IDF 벡터화
    tfidf_vect = TfidfVectorizer()
    tfidf_matrix = tfidf_vect.fit_transform([input_item] + model.columns.astype(str).tolist())

    # 코사인 유사도 계산
    cosine_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    df_cosine = pd.DataFrame(cosine_matrix, index=['input_item'] + model.columns.astype(str).tolist(),
                             columns=['input_item'] + model.columns.astype(str).tolist())

    # 입력 아이템에 대한 유사한 아이템 10개 추출
    input_item_id = 'input_item'
    recommended_items = df_cosine.loc[df_cosine[input_item_id] < 1, input_item_id].nlargest(11).index[1:]

    # 추천된 아이템 리스트
    recommended_item_list = [{'index': index, 'item_name': f'매물번호 {index}'} for index in recommended_items]
    return recommended_item_list

   # 추천된 아이템이 10개 미만인 경우에 대한 처리
    if len(recommended_item_list) < 10:
        pass

    return recommended_item_list

def cosine_similarity_view(request, index):
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
    recommended_items = cosine_similarity_maemul(input_item, loaded_model)

    context = {
        'input_item': input_item,
        'recommended_items': recommended_items,
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
