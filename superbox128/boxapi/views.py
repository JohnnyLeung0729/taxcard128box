from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, hlo):
    return HttpResponse('app 第一个玩%s魔快' % hlo)

def search(request, hlo):
    return HttpResponse("测试结果是 %s 这样的" % hlo)