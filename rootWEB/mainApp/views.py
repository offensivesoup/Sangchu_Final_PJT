from django.shortcuts import render
from django.db import connections, connection
from django.http import JsonResponse, HttpResponse
from django.views import View
import pandas as pd
import numpy as np
import joblib
from joblib import load
import os


def index(request) :
    print('debug >>> client path, mainApp/index, render = index')
    return render(request, 'main/index.html')

def map(request) :
    return render(request, 'main/map.html')

# Create your views here.
def sign2(request):
    return render(request,'main/sign2.html')

def busan(request):
    print('debug >>> client path, mainApp/busan, render = busan')
    return render(request,'main/busan.html')