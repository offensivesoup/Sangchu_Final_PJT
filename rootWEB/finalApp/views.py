from django.shortcuts import render

# Create your views here.
def list(request):
    print('debug >>> client path, finalApp/list, render = list')
    return render(request,'final/list.html')

def detail(request,maemul_id):
    print('debug >>> maemul_id: ',maemul_id)
    print('debug >>> client path, finalApp/detail, render = detail')
    return render(request, 'final/detail.html')