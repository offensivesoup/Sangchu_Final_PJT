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
    return render(request, 'region/index.html', {'region_name': region_name})

