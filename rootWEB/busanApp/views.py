from django.shortcuts import render
from django.db import connection, connections
from django.http import JsonResponse
from django.views import View

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
