from django.shortcuts import render
from django.http import HttpResponse
from .models import Information
from .models import Portinfo
from django.http import HttpRequest
import uuid

# Create your views here.
def index(request):
    return HttpResponse('app 第一个玩魔快')

def initsys(request, hlo):
    obj=Information(infocode='helloworld',iname='Johnny',ivalue='cool',status=1,memo='gogogo')
    obj.save()
    return HttpResponse("initsys测试结果是 %s 这样的" % hlo)

def scanboard(request, hlo):
    return HttpResponse("scanboard测试结果是 %s 这样的" % hlo)

def getsysinfo(request, hlo):
    return HttpResponse("getsysinfo测试结果是 %s 这样的" % hlo)

#分享指定设备，并更新数据库对应端口状态
def sharedevice(request, hlo):
    return HttpResponse("sharedevice测试结果是 %s 这样的" % hlo)

def disconnectdevice(request, hlo):
    return HttpResponse("disconnectdevice测试结果是 %s 这样的" % hlo)

def scandevice(request, hlo):
    return HttpResponse("scandevice测试结果是 %s 这样的" % hlo)

def rebootdevice(request, hlo):
    return HttpResponse("rebootdevice测试结果是 %s 这样的" % hlo)

def resetdevice(request, hlo):
    return HttpResponse("resetdevice测试结果是 %s 这样的" % hlo)

def setdevice(request, hlo):
    return HttpResponse("setdevice测试结果是 %s 这样的" % hlo)

def regenterinfo(request):  
    print('测试句子是否正确')
    if request.method=='GET':
        concat = request.POST
        postbody = request.body
        print(concat)
        print(postbody)
    else:
        tempstr = request.POST.get('iv','')
        print(tempstr)
    return HttpResponse("测试POST数据接收" + tempstr)

def signmachine(request):
    return HttpResponse("设备签到接口")

#添加新的设备端口到数据库，属于后台代码
def addnewport(request):
    pi=0
    pn='null'
    if request.method=='GET':
        print('un GET')
    else:
        pi = request.POST.get('pi',0)
        pn = request.POST.get('pn','null')
        
    obj=Portinfo(portindex=pi,portname=pn,pcode=uuid.uuid1())   #在这里需要生成uuid提供给ID，否则内部model会默认生成重复uuid
    obj.save()
    return HttpResponse("添加新的设备接口")

def listport(reuqest):
    return HttpResponse("获取所有接口和状态列表")

#根据纳税人识别号，及相关信息查询对应配置的接口
def getportbynsrsbh(request):
    nsrsbh='null'
    codekey='01010101'
    if request.method=='GET':
        print('un GET')
    else:
        nsrsbh = request.POST.get('nsrsbh','null')
        codekey = request.POST.get('codekey','01010101')
        
        obj=Portinfo.objects.filter(entcode=nsrsbh)
        for iobj in obj:
            print(iobj.entname)  
    return HttpResponse("返回接口信息"+nsrsbh+codekey)

#绑定更新接口企业信息
def bandupdateportinfo(request):
    portinfo='null'
    codekey='01010101'
    entname='null'
    entcode='null'
    if request.method=='GET':
        print('un GET')
    else:
        portinfo = request.POST.get('portinfo','null')
        codekey = request.POST.get('codekey','01010101')
        entname = request.POST.get('entname','null')
        entcode = request.POST.get('entcode','null')
        print(entname) 
        
    return HttpResponse("绑定更新企业")