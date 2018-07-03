from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.


def index(request):
    # 请求路径和方法
    print(request.path,request.method)
    # 请求头的元信息 和get 请求参数(查询参数)
    print(request.META,request.GET)
    print(request.GET.get('page'),request.GET.get('tag'))
    # POST 请求参数(表单参数）
    print(request.POST)
    # return HttpResponse
    return render(request,'art/list.html',{'name':'yt','age':10})
    # return JsonResponse({'name':'delattr'})
