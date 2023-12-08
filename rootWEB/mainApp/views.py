from django.shortcuts import render
def index(request) :
    print('debug >>> client path, mainApp/index, render = index')
    return render(request, 'main/index.html')

# Create your views here.
