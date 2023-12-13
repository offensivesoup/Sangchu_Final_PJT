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
def busan(request):
    print('debug >>> client path, mainApp/busan, render = busan')
    return render(request,'main/busan.html')


def analysis_lease(request):
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
        # gu = [data[i]['index'] for i in range(len(data))]
        # year = [i for i in range(2014,2023)]


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
    return JsonResponse({'data': final_dict }, safe=False)