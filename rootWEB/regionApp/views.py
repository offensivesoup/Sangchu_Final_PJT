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

def index(request) :
    print('debug >>> client path, regionApp/index, render = index')
    return render(request, 'region/index.html')

def get_region_type_data(request):
    with connection.cursor() as cursor:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM reigon_type_count")
            # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            type = [data[i]['type'] for i in range(len(data))]
            jingucnt = [data[i]['jingu'] for i in range(len(data))]
            haeundaegucnt = [data[i]['haeundaegu'] for i in range(len(data))]
            jungucnt = [data[i]['jungu'] for i in range(len(data))]
            dongnaegucnt = [data[i]['dongnaegu'] for i in range(len(data))]
            sasangucnt = [data[i]['sasangu'] for i in range(len(data))]
            dongucnt = [data[i]['dongu'] for i in range(len(data))]
            sahagucnt = [data[i]['sahagu'] for i in range(len(data))]
            gyuemjungucnt = [data[i]['gyuemjungu'] for i in range(len(data))]
            gijangcnt = [data[i]['gijang'] for i in range(len(data))]
            bukgucnt = [data[i]['bukgu'] for i in range(len(data))]
            namgucnt = [data[i]['namgu'] for i in range(len(data))]
            suyoungucnt = [data[i]['suyoungu'] for i in range(len(data))]
            yeonjegucnt = [data[i]['yeonjegu'] for i in range(len(data))]
            gangseogucnt = [data[i]['gangseogu'] for i in range(len(data))]
            seogucnt = [data[i]['seogu'] for i in range(len(data))]
            youngdogucnt = [data[i]['youngdogu'] for i in range(len(data))]

            jinguDict = { name : value for name, value in zip(type,jingucnt)}
            haeundaeguDict = {name: value for name, value in zip(type, haeundaegucnt)}
            junguDict = {name: value for name, value in zip(type, jungucnt)}
            dongnaeguDict = {name: value for name, value in zip(type, dongnaegucnt)}
            sasanguDict = {name: value for name, value in zip(type, sasangucnt)}
            donguDict = {name: value for name, value in zip(type, dongucnt)}
            sahaguDict = {name: value for name, value in zip(type, sahagucnt)}
            gyuemjunguDict = {name: value for name, value in zip(type, gyuemjungucnt)}
            gijangDict = {name: value for name, value in zip(type, gijangcnt)}
            bukguDict = {name: value for name, value in zip(type, bukgucnt)}
            namguDict = {name: value for name, value in zip(type, namgucnt)}
            suyounguDict = {name: value for name, value in zip(type, suyoungucnt)}
            yeonjeguDict = {name: value for name, value in zip(type, yeonjegucnt)}
            gangseoguDict = {name: value for name, value in zip(type, gangseogucnt)}
            seoguDict = {name: value for name, value in zip(type, seogucnt)}
            youngdoguDict = {name: value for name, value in zip(type, youngdogucnt)}

            return JsonResponse({'jingu': jinguDict, 'haeundaegu' : haeundaeguDict, 'jungu' : junguDict,
                                 "dongnaegu" : dongnaeguDict, 'sasangu' : sasanguDict, 'dongu' : donguDict,
                                 'sahagu' : sahaguDict, 'gyumjungu' : gyuemjunguDict, 'gijang' : gijangDict,
                                 'bukgu' : bukguDict, 'namgu' : namguDict, 'suyoungu' : suyounguDict,
                                 'yeonjegu' : yeonjeguDict, 'gangseogu' : gangseoguDict,
                                 "seogu" : seoguDict, "youngdogu" : youngdoguDict}, safe=False)