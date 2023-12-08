from django.shortcuts import render
from django.db import connections

def fetch_lease_trend_view(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM lease_trend")
        lease_trend = cursor.fetchall()

    return render(request, 'busan/index.html', {'lease_trend': lease_trend})

def fetch_zipgac_numbers_view(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM zipgac_numbers")
        zipgac_numbers = cursor.fetchall()

    return render(request, 'busan/index.html', {'zipgac_numbers': zipgac_numbers})

def fetch_population_info_view(request):
    with connections['default'].cursor() as cursor:
         cursor.execute("SELECT * FROM reigon_type_count")
         population_info = cursor.fetchall()
         return render(request, 'busan/index.html', {'population_info': population_info})

def fetch_store_density_view(request) :
    print('debug >>> client path, mainApp/index, render = index')
    with connections['default'].cursor() as cursor:
        sql_query = "SELECT * FROM store_density"
        cursor.execute(sql_query)
        store_density = cursor.fetchall()
    return render(request, 'busan/index.html', {'store_density': store_density})