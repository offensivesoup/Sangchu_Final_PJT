from django.shortcuts import render
from django.db import connections

# Create your views here.
def fetch_population_info_view(request):
    with connections['default'].cursor() as cursor:
         cursor.execute("SELECT * FROM reigon_type_count")
         population_info = cursor.fetchall()

        return render(request, 'busan/index.html', {'population_info': population_info})