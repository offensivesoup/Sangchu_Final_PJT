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

def detail(request, region_name,maemul_id):
    print('debug >>> region_name: ', region_name)
    print('debug >>> maemul_id: ',maemul_id)
    print('debug >>> client path, finalApp/detail, render = detail')
    return render(request, 'final/detail.html')


def get_list(request,region_name):
    region_name = region_name

    sql_query = "SELECT * FROM empty_room_data WHERE address = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql_query,(region_name,))
        result = cursor.fetchall()
        data = []
        for row in result:
            name = {'index':row[16],'address': row[5],'deposit':row[0],'month':row[1],'criteria':row[2],'lat':row[3],'lng':row[4],'area':row[7],'my_area':row[8],
                    'my_floor':row[9],'total_floor':row[10]}
            data.append(name)


        # # 쿼리 결과를 필요한 형식으로 가공
        # columns = [col[0] for col in cursor.description]
        # print(columns)
        # data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        # data = {'gu':'기장군','value':7}
    return JsonResponse({'data': data})



def get_detail(request,region_name,maemul_id):



    return JsonResponse({'data':data})