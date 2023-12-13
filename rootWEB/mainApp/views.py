from django.shortcuts import render
def index(request) :
    print('debug >>> client path, mainApp/index, render = index')
    return render(request, 'main/index.html')

def map(request) :
    return render(request, 'main/map.html')

# Create your views here.
def busan(request):
    print('debug >>> client path, mainApp/busan, render = busan')
    return render(request,'main/busan.html')