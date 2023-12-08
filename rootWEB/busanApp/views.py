from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db import connections

def fetch_store_density_view(request) :
    print('debug >>> client path, mainApp/index, render = index')
    with connections['default'].cursor() as cursor:
        # SQL 쿼리 작성
        sql_query = "SELECT * FROM store_density"

        # SQL 쿼리 실행
        cursor.execute(sql_query)

        # 결과 가져오기
        store_density = cursor.fetchall()
    # result에는 테이블의 모든 데이터가 포함되어 있습니다.
    # 원하는 대로 이 데이터를 활용할 수 있습니다.
    return render(request, 'busan/index.html', {'store_density': store_density})