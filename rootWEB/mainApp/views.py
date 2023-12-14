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

def signup(request):
    return render(request, 'main/signup.html')
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