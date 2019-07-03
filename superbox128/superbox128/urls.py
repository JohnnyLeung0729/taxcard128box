"""superbox128 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from boxapi import views as ba
#pattern: /^[a-z0-9A-Z._%]+$/ ; 


"""
signmachine  签到机器，开始进行操作，有效期30分钟，超过30分钟需要再次签到。
addnewport   添加机器主板接口
listport     获取所有接口及状态列表
getportbynsrsbh  根据纳税人识别号获取接口信息
bandupdateportinfo  绑定更新企业对应端口信息
"""

urlpatterns = [
    url(r'^boxapi/initsys/(?P<hlo>[a-z0-9A-Z._%]+)/', ba.initsys),
    url(r'^boxapi/scanboard/(?P<hlo>[a-z0-9A-Z._%]+)/', ba.scanboard),
    url(r'^boxapi/getsysinfo/(?P<hlo>[a-z0-9A-Z._%]+)/', ba.getsysinfo),
    url(r'^boxapi/sharedevice/(?P<hlo>[a-z0-9A-Z._%]+)/', ba.sharedevice),
    url(r'^boxapi/disconnectdevice/(?P<hlo>[a-z0-9A-Z._%]+)/', ba.disconnectdevice),
    url(r'^boxapi/scandevice/(?P<hlo>[a-z0-9A-Z._%]+)/', ba.scandevice),
    url(r'^boxapi/rebootdevice/(?P<hlo>[a-z0-9A-Z._%]+)/', ba.rebootdevice),
    url(r'^boxapi/resetdevice/(?P<hlo>[a-z0-9A-Z._%]+)/', ba.resetdevice),
    url(r'^boxapi/setdevice/(?P<hlo>[a-z0-9A-Z._%]+)/', ba.setdevice),
    url(r'^boxapi/regenterinfo/', ba.regenterinfo),
    url(r'^boxapi/signmachine/', ba.signmachine),
    url(r'^boxapi/addnewport/', ba.addnewport),
    url(r'^boxapi/listport/', ba.listport),
    url(r'^boxapi/getportbynsrsbh/', ba.getportbynsrsbh),
    url(r'^boxapi/bandupdateportinfo/', ba.bandupdateportinfo),
    url(r'^boxapi/', ba.index),
]
