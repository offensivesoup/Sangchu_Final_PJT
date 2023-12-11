from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views import View

def fetch_lease_trend_view(request):
    with connection['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM lease_trend")
        lease_trend = cursor.fetchall()

    return render(request, 'busan/index.html', {'lease_trend': lease_trend})

def fetch_zipgac_number_view(request):
    with connection['default'].cursor() as cursor:
        sql_query = "SELECT * FROM zipgac_number_copy"
        cursor.execute(sql_query)
        zipgac_number = cursor.fetchall()

    return render(request, 'busan/index.html', {'zipgac_number': zipgac_number})

def fetch_population_info_view(request):
    with connection['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM reigon_type_count")
        population_info = cursor.fetchall()
    return render(request, 'busan/index.html', {'population_info': population_info})

def fetch_store_density_view(request) :
    print('debug >>> client path, mainApp/index, render = index')
    with connection['default'].cursor() as cursor:
        sql_query = "SELECT * FROM store_density"
        cursor.execute(sql_query)
        store_density = cursor.fetchall()
    return render(request, 'busan/index.html', {'store_density': store_density})

# 2023-12-11 store_density를 json형식으로 html로 가져오기
def json_store_density_view(request) :
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM store_density")

        # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # JSON 형식으로 응답
    return JsonResponse({'data': data}, safe=False)

def json_lease_trend_view(request) :
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM lease_trend")

        # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # JSON 형식으로 응답
    return JsonResponse({'data': data}, safe=False)

def json_zipgac_number_view(request) :
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM zipgac_number")

        # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # JSON 형식으로 응답
    return JsonResponse({'data': data}, safe=False)

def json_population_info_view(request) :
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM population_info")

        # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # JSON 형식으로 응답
    return JsonResponse({'data': data}, safe=False)