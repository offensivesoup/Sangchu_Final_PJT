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

def index(request,region_name) :
    region_name = region_name
    print('deubg >>> region_name: ' ,region_name)
    print('debug >>> client path, regionApp/index, render = index')
    return render(request, 'region/index.html')

def zipgac_number_chart(request):
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

    chart_data = {
        'chart': {
            'type': 'bar'
        },
        'title': {
            'text': '구별 집객시설 수'
        },
        'xAxis': {
            'categories': final_dict['gu'],
            'title': {
                'text': '구'
            }
        },
        'yAxis': {
            'title': {
                'text': '시설 수'
            }
        },
        'series': [{
            'name': '시설 수',
            'data': final_dict['number']
        }]
    }

    return render(request, 'region/chart1.html', {'chart_data': chart_data})