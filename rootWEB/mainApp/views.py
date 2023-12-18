from django.shortcuts import render
from django.db import connections, connection
from django.http import JsonResponse, HttpResponse
from django.views import View
import pandas as pd
import numpy as np
import joblib
from joblib import load
import os


def index(request) :
    print('debug >>> client path, mainApp/index, render = index')
    return render(request, 'main/index.html')

def map(request) :
    return render(request, 'main/map.html')

# Create your views here.
def sign2(request):
    return render(request,'main/sign2.html')


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

        processed_data = [{'name': '집객시설 수', 'data': number_values}]

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

    return JsonResponse({'data': data})
