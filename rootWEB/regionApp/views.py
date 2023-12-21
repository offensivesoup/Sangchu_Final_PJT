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

def index(request, region_name) :
    region_name = region_name
    print('deubg >>> region_name: ' ,region_name)
    print('debug >>> client path, regionApp/index, render = index')
    return render(request, 'region/index.html', {'region_name': region_name})

## 주요 상권 설명

def get_information_main_data(request, region_name):
    if region_name == "강서구":
        contents = "강서구(Gangseo-gu): 부산의 서쪽에 위치하며, 인프라와 산업시설이 발달해 있는 지역."
    elif region_name == "사상구":
        contents = "사상구(Sasang-gu): 국내 최대의 물류 단지인 부산진로와 가깝고, 산업 지역."
    elif region_name == "중구":
        contents = "중구(Jung-gu): 부산의 중심지로서 남포동과 국제시장 등이 위치하고 있습니다. 역사적인 명소와 번화가가 공존하는 지역."
    elif region_name == "서구":
        contents = "서구(Seo-gu): 부산역과 부산진역이 위치하는 교통 중심지로, 상업 및 주거 지역이 혼재되어 있음."
    elif region_name == "동구":
        contents = "동구(Dong-gu): 대표적인 명소로는 이기대 동래문 및 부산 시립미술관이 있습니다. 자연환경이 풍부한 구."
    elif region_name == "영도구":
        contents = "영도구(Yeongdo-gu): 부산항이 위치하고 있어 수산물 시장이 발달한 지역이며, 독특한 느낌의 역사적인 지구."
    elif region_name == "부산진구":
        contents = "부산진구(Busanjin-gu): 대중교통이 발달하고 서면과 인접해 있어 상업 및 유흥 시설이 밀집."
    elif region_name == "동래구":
        contents = "동래구(Dongnae-gu): 자연환경이 풍부하며 동래읍성과 동래수목원 등이 위치해 관광 명소로 알려져 있음."
    elif region_name == "남구":
        contents = "남구(Nam-gu): 해운대와 가까워 해변과 함께 자연 경관을 즐길 수 있는 구, 또한 대학가로도 유명."
    elif region_name == "북구":
        contents = "북구(Buk-gu): 대학로가 위치해 있고, 서구와 함께 교통 중심지로 알려져 있음."
    elif region_name == "해운대구":
        contents = "해운대구(Haeundae-gu): 국내외에서 많은 관광객이 찾는 지역으로 해수욕, 호텔, 리조트 등이 발달."
    elif region_name == "사하구":
        contents = "사하구(Saha-gu): 인프라 개발이 활발히 이루어지고 있으며, 대중교통이 향상된 구."
    elif region_name == "금정구":
        contents = "금정구(Geumjeong-gu): 부산의 북동쪽에 위치하며, 부산의 중심지와는 거리가 있지만 자연환경이 풍부한 구."
    elif region_name == "연제구":
        contents = "연제구(Yeonje-gu): 주택가가 많이 있고 교육 기관도 밀집해 있는 지역."
    elif region_name == "수영구":
        contents = "수영구(Suyeong-gu): 해운대와 인접하며 해수욕과 관련된 시설이 많이 위치한 지역."
    elif region_name == "기장군":
        contents = "기장군(Gijang-gun): 부산의 동쪽에 위치하며, 해변과 자연 경관이 아름다운 곳으로 최근 관광 및 레저 산업이 활성화되고 있음."
    return JsonResponse({'data': contents}, safe=False)
## 업종별 상권 수
def get_region_type_data(request, region_name):
    with connection.cursor() as cursor:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM reigon_type_count")
            # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            type = [data[i]['type'] for i in range(len(data))]
            jingucnt = [data[i]['부산진구'] for i in range(len(data))]
            haeundaegucnt = [data[i]['해운대구'] for i in range(len(data))]
            jungucnt = [data[i]['중구'] for i in range(len(data))]
            dongnaegucnt = [data[i]['동래구'] for i in range(len(data))]
            sasangucnt = [data[i]['사상구'] for i in range(len(data))]
            dongucnt = [data[i]['동구'] for i in range(len(data))]
            sahagucnt = [data[i]['사하구'] for i in range(len(data))]
            gyuemjungucnt = [data[i]['금정구'] for i in range(len(data))]
            gijangcnt = [data[i]['기장군'] for i in range(len(data))]
            bukgucnt = [data[i]['북구'] for i in range(len(data))]
            namgucnt = [data[i]['남구'] for i in range(len(data))]
            suyoungucnt = [data[i]['수영구'] for i in range(len(data))]
            yeonjegucnt = [data[i]['연제구'] for i in range(len(data))]
            gangseogucnt = [data[i]['강서구'] for i in range(len(data))]
            seogucnt = [data[i]['서구'] for i in range(len(data))]
            youngdogucnt = [data[i]['영도구'] for i in range(len(data))]

            부산진구 = { name : value for name, value in zip(type,jingucnt)}
            해운대구 = {name: value for name, value in zip(type, haeundaegucnt)}
            중구 = {name: value for name, value in zip(type, jungucnt)}
            동래구 = {name: value for name, value in zip(type, dongnaegucnt)}
            사상구 = {name: value for name, value in zip(type, sasangucnt)}
            동구 = {name: value for name, value in zip(type, dongucnt)}
            사하구 = {name: value for name, value in zip(type, sahagucnt)}
            금정구 = {name: value for name, value in zip(type, gyuemjungucnt)}
            기장군 = {name: value for name, value in zip(type, gijangcnt)}
            북구 = {name: value for name, value in zip(type, bukgucnt)}
            남구 = {name: value for name, value in zip(type, namgucnt)}
            수영구 = {name: value for name, value in zip(type, suyoungucnt)}
            연제구 = {name: value for name, value in zip(type, yeonjegucnt)}
            강서구 = {name: value for name, value in zip(type, gangseogucnt)}
            서구 = {name: value for name, value in zip(type, seogucnt)}
            영도구 = {name: value for name, value in zip(type, youngdogucnt)}

            final_dict = {'부산진구': 부산진구, '해운대구': 해운대구, '중구': 중구,
             "동래구": 동래구, '사상구': 사상구, '동구': 동구,
             '사하구': 사하구, '금정구': 금정구, '기장군': 기장군,
             '북구': 북구, '남구': 남구, '수영구': 수영구,
             '연제구': 연제구, '강서구': 강서구,
             "서구": 서구, "영도구": 영도구}

            final_dict_keys = [i for i in final_dict[region_name].keys()]
            final_dict_values = [i for i in final_dict[region_name].values()]
            result = {'region' : region_name, "category" : final_dict_keys, "cnt" : final_dict_values}
            return JsonResponse({'data' : result}, safe=False)


def get_time_day_age_people_data(request, region_name):
    with connection.cursor() as cursor:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM time_day_age_people")
            # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            ## 해당 gu의 데이터를 가져온다.
            matching_data = next((item for item in data if item["gu"] == region_name), None)
            result_list = [
                ["구", matching_data.get("구")],
                ["오전", float(matching_data.get("오전", 0))],
                ["오후", float(matching_data.get("오후", 0))],
                ["저녁", float(matching_data.get("저녁", 0))],
                ["월요일", float(matching_data.get("월요일", 0))],
                ["화요일", float(matching_data.get("화요일", 0))],
                ["수요일", float(matching_data.get("수요일", 0))],
                ["목요일", float(matching_data.get("목요일", 0))],
                ["금요일", float(matching_data.get("금요일", 0))],
                ["토요일", float(matching_data.get("토요일", 0))],
                ["일요일", float(matching_data.get("일요일", 0))],
                ["10대", float(matching_data.get("10대", 0))],
                ["20대", float(matching_data.get("20대", 0))],
                ["30대", float(matching_data.get("30대", 0))],
                ["40대", float(matching_data.get("40대", 0))],
                ["50대", float(matching_data.get("50대", 0))],
                ["60대", float(matching_data.get("60대", 0))],
                ["70대", float(matching_data.get("70대", 0))]
            ]

            timeLst = result_list[1:4]
            dayLst  = result_list[4:11]
            ageLst  = result_list[11:]

    return JsonResponse({'ageLst' : ageLst, 'timeLst' : timeLst, 'dayLst' : dayLst}, safe=False)

def get_final_moving_data(request, region_name):
    with connection.cursor() as cursor:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM final_moving")
            # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            ## 해당 gu의 데이터를 가져온다.
            matching_data = next((item for item in data if item["gu"] == region_name), None)
            result = [float(value) for key, value in matching_data.items() if key != "gu"]

    return JsonResponse({'data' : result}, safe=False)

def get_rent_mean_data(request, region_name):
    ayears_list = []
    byears_list = []
    cyears_list = []
    dyears_list = []
    eyears_list = []
    result_list = []
    with connection.cursor() as cursor:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM rent_mean")
            # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            ## 해당 gu의 데이터를 가져온다.
            # matching_data = next((item for item in data if item["gu"].strip() == region_name), None)
            matching_data_list = [item for item in data if item["gu"].strip() == region_name]
            years_data = [
                {year: float(item[year]) if item[year].replace(".", "").isdigit() else None
                 for year in ["2018", "2019", "2020", "2021", "2022"]}
                for item in matching_data_list
            ]
            for i in range(len(years_data)):
                result_list.append(years_data[i])
                ayears_list = []
                byears_list = []
                cyears_list = []
                dyears_list = []
                eyears_list = []
                for m in result_list:
                    ayears_list.append(m['2018'])
                    byears_list.append(m['2019'])
                    cyears_list.append(m['2020'])
                    dyears_list.append(m['2021'])
                    eyears_list.append(m['2022'])
            return JsonResponse({'building' : [i['building'] for i in matching_data_list], 'a' : ayears_list, 'b' : byears_list, 'c' : cyears_list, 'd' : dyears_list, 'e' : eyears_list}, safe=False)

def get_subway_session_data(request, region_name):
    with connection.cursor() as cursor:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM subway_session_population")
            # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            matching_data_list = [item for item in data if item["gu"].strip() == region_name]
            station_list = [entry["station"] for entry in matching_data_list]
            sum_list = [float(entry["sum"]) for entry in matching_data_list]
            return JsonResponse({'station': station_list, 'sum' : sum_list}, safe=False)

def get_eval_score_data(request, region_name):
    with connection.cursor() as cursor:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM eval_score")
            # 쿼리 결과를 필요한 형식으로 가공 (예: 딕셔너리 리스트)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            matching_data = next((item for item in data if item["gu"].strip() == region_name), None)
            matching_data_list = [item for item in data if item["gu"].strip() == region_name]
            category_list = [entry["category"] for entry in matching_data_list]
            marketability_list = [float(entry["marketability"]) for entry in matching_data_list]
            potential_list = [float(entry["potential"]) for entry in matching_data_list]
            stability_list = [float(entry["stability"]) for entry in matching_data_list]
            floating_list = [float(entry["floating_population_market"]) for entry in matching_data_list]
            return JsonResponse({'marketability' : marketability_list, 'category' : category_list,
                                 'potential' : potential_list, 'stability' : stability_list, 'floating' : floating_list}, safe=False)

def get_center_coordinates(gu):
    gu_coordinates = {
        "기장군": (35.244394201041416, 129.2227421459612),
        "해운대구": (35.162995101348564, 129.16356675415742),
        "수영구": (35.145458076325326, 129.11307922758124),
        "남구": (35.136262710025456, 129.08468141230728),
        "연제구": (35.176129771565535, 129.079712017898),
        "동구": (35.129161209712215, 129.04558174709652),
        "중구": (35.10621258919303, 129.03247914653906),
        "서구": (35.09784717231878, 129.0242833944746),
        "영도구": (35.090989265185435, 129.06778927857764),
        "부산진구": (35.162697533668855, 129.05307148933218),
        "동래구": (35.196701579922234, 129.09391527580505),
        "금정구": (35.24278952025912, 129.09242514119632),
        "북구": (35.196830935641835, 128.99036558066425),
        "사상구": (35.15288084181415, 128.99035858685488),
        "사하구": (35.104261135161906, 128.97500193638786),
        "강서구": (35.21179065375177, 128.98045854324366),
    }

    return gu_coordinates.get(gu, (0, 0))

def school_json(request, region_name):
    try:
        # GET 요청에서 'gu' 매개변수의 값을 추출합니다.
        # gu = request.GET.get('gu', None)

        # 'gu'를 사용하여 중심 좌표를 가져옵니다.
        center_latitude, center_longitude = get_center_coordinates(region_name)

        # 데이터베이스 커서를 사용하여 SQL 쿼리를 실행합니다.
        with connection.cursor() as cursor:
            # 'gu'에 따라 필터링된 쿼리를 실행합니다.
            cursor.execute(
                "SELECT gu, name, address, category, type, est, lat, lng FROM school_lat_lng where gu=%s",[region_name])
            # 실행된 쿼리에서 모든 결과를 가져옵니다.
            locations = cursor.fetchall()

        # 가져온 데이터를 JSON 직렬화 가능한 형식으로 처리합니다.
        data = [
            {
                "gu": location[0],
                "name": location[1],
                "address": location[2],
                "category": location[3],
                "type": location[4],
                "est": location[5],
                "lat": location[6],
                "lng": location[7],
            }
            for location in locations
        ]

        # 처리된 데이터와 중심 좌표를 포함한 JSON 응답을 반환합니다.
        return JsonResponse({"data": data, "center_latitude": center_latitude, "center_longitude": center_longitude},
                            safe=False)

    except Exception as e:
        # 예외가 발생하면 에러 메시지를 포함한 500 상태의 JSON 응답을 반환합니다.
        return JsonResponse({"error": str(e)}, status=500)

def subwayloc_json(request, region_name):
    try:
        # GET 요청에서 'gu' 매개변수의 값을 추출합니다.
        gu = request.GET.get('gu', None)

        # 'gu'를 사용하여 중심 좌표를 가져옵니다.
        center_latitude, center_longitude = get_center_coordinates(region_name)

        # 데이터베이스 커서를 사용하여 SQL 쿼리를 실행합니다.
        with connection.cursor() as cursor:
            # 'gu'에 따라 필터링된 쿼리를 실행합니다.
            cursor.execute("SELECT l.gu, l.sang_name, l.subway_name, l.lat, l.lng, round(p.sum, 1) FROM subway_lat_lng l INNER JOIN subway_session_population p ON l.subway_name = p.station WHERE l.gu = %s", [region_name])
            # 실행된 쿼리에서 모든 결과를 가져옵니다.
            locations = cursor.fetchall()

        # 가져온 데이터를 JSON 직렬화 가능한 형식으로 처리합니다.
        data = [
            {
                "gu": location[0],
                "sang_name": location[1],
                "subway_name": location[2],
                "lat": location[3],
                "lng": location[4],
                "sum": location[5],
            }
            for location in locations
        ]

        # 처리된 데이터와 중심 좌표를 포함한 JSON 응답을 반환합니다.
        return JsonResponse({"data": data, "center_latitude": center_latitude, "center_longitude": center_longitude}, safe=False)

    except Exception as e:
        # 예외가 발생하면 에러 메시지를 포함한 500 상태의 JSON 응답을 반환합니다.
        return JsonResponse({"error": str(e)}, status=500)
