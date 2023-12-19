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
def list(request,region_name):
    region_name = region_name
    print('debug >>> client path, finalApp/list, render = list')
    return render(request,'final/list.html',{'region_name':region_name})

def detail(request,maemul_id):
    print('debug >>> maemul_id: ',maemul_id)
    print('debug >>> client path, finalApp/detail, render = detail')
    return render(request, 'final/detail.html')


def get_list(request,region_name):
    region_name = region_name

    # sql_query = "SELECT index,address,deposit,montly,division,lease_area,my_area FROM empty_room_data"
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM empty_room_data")
        result = cursor.fetchall()
        data = []
        print(result[3][1])

        # 쿼리 결과를 필요한 형식으로 가공
        columns = [col[0] for col in cursor.description]
        print(columns)
        # data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        data = {'gu':'기장군','value':7}
    return JsonResponse({'data': data})