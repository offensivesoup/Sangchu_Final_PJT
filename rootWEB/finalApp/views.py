from django.shortcuts import render

# Create your views here.
def list(request):
    print('debug >>> client path, finalApp/list, render = list')
    return render(request,'final/list.html')