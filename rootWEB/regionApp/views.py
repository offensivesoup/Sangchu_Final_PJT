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

# Create your views here.
# 구별 분석 페이지로 이동

def index(request, region_name) :
    region_name = region_name
    print('deubg >>> region_name: ' ,region_name)
    print('debug >>> client path, regionApp/index, render = index')
    return render(request, 'region/index.html', {'region_name': region_name})

##
ifDict = {}
def get_region_type_data(request, region_name):
    with connection.cursor() as cursor:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM reigon_type_count")
            # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            type = [data[i]['type'] for i in range(len(data))]
            jingucnt = [data[i]['부산진구'] for i in range(len(data))]
            haeundaegucnt = [data[i]['해운대구'] for i in range(len(data))]
            jungucnt = [data[i]['중구'] for i in range(len(data))]
            dongnaegucnt = [data[i]['동래구'] for i in range(len(data))]
            sasangucnt = [data[i]['사상구'] for i in range(len(data))]
            dongucnt = [data[i]['동구'] for i in range(len(data))]
            sahagucnt = [data[i]['사하구'] for i in range(len(data))]
            gyuemjungucnt = [data[i]['금정구'] for i in range(len(data))]
            gijangcnt = [data[i]['기장군'] for i in range(len(data))]
            bukgucnt = [data[i]['북구'] for i in range(len(data))]
            namgucnt = [data[i]['남구'] for i in range(len(data))]
            suyoungucnt = [data[i]['수영구'] for i in range(len(data))]
            yeonjegucnt = [data[i]['연제구'] for i in range(len(data))]
            gangseogucnt = [data[i]['강서구'] for i in range(len(data))]
            seogucnt = [data[i]['서구'] for i in range(len(data))]
            youngdogucnt = [data[i]['영도구'] for i in range(len(data))]

            부산진구 = { name : value for name, value in zip(type,jingucnt)}
            해운대구 = {name: value for name, value in zip(type, haeundaegucnt)}
            중구 = {name: value for name, value in zip(type, jungucnt)}
            동래구 = {name: value for name, value in zip(type, dongnaegucnt)}
            사상구 = {name: value for name, value in zip(type, sasangucnt)}
            동구 = {name: value for name, value in zip(type, dongucnt)}
            사하구 = {name: value for name, value in zip(type, sahagucnt)}
            금정구 = {name: value for name, value in zip(type, gyuemjungucnt)}
            기장군 = {name: value for name, value in zip(type, gijangcnt)}
            북구 = {name: value for name, value in zip(type, bukgucnt)}
            남구 = {name: value for name, value in zip(type, namgucnt)}
            수영구 = {name: value for name, value in zip(type, suyoungucnt)}
            연제구 = {name: value for name, value in zip(type, yeonjegucnt)}
            강서구 = {name: value for name, value in zip(type, gangseogucnt)}
            서구 = {name: value for name, value in zip(type, seogucnt)}
            영도구 = {name: value for name, value in zip(type, youngdogucnt)}

            final_dict = {'부산진구': 부산진구, '해운대구': 해운대구, '중구': 중구,
             "동래구": 동래구, '사상구': 사상구, '동구': 동구,
             '사하구': 사하구, '금정구': 금정구, '기장군': 기장군,
             '북구': 북구, '남구': 남구, '수영구': 수영구,
             '연제구': 연제구, '강서구': 강서구,
             "서구": 서구, "영도구": 영도구}

            final_dict_keys = [i for i in final_dict[region_name].keys()]
            final_dict_values = [i for i in final_dict[region_name].values()]
            result = {'region' : region_name, "category" : final_dict_keys, "cnt" : final_dict_values}
            return JsonResponse({'data' : result}, safe=False)

def chart_float_pop(request,region_name):
    print('debug >>>>>> chart_float_pop ')
    print('debug >>>>>> region: ',region_name)
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT gu, popu_density FROM population_info")
    #     columns = [col[0] for col in cursor.description]
    #     data = [dict(zip(columns, row)) for row in cursor.fetchall()]
    data = {'name': '기장군', 'value': 7}
    return JsonResponse({'data': data})
