from django.db import models
import uuid

# Create your models here.
class Information(models.Model):
    infocode = models.CharField('infocode', max_length=64, primary_key=True)
    iname = models.CharField('iname', max_length=48)
    ivalue = models.CharField('ivalue', max_length=254)
    status = models.IntegerField('status')
    memo = models.CharField('memo', max_length=128)
    
    def __str__(self):
        return self.infocode
    
    class Meta:
        db_table='information'
        
        
class Portinfo(models.Model):
    pcode = models.CharField('pcode',max_length=64,primary_key=True,default=uuid.uuid1())
    portindex = models.IntegerField('portindex')
    portname = models.CharField('portname',max_length=32,default='null')
    entname = models.CharField('entname',max_length=64,default='空')
    entcode = models.CharField('entcode',max_length=64,default='000000000000000000')
    status = models.IntegerField('status',default=9)
    model = models.CharField('model',max_length=8,default='null')
    condatetime = models.DateTimeField('condatetime',auto_now_add=True)
    memo = models.CharField('memo',max_length=254,default='')
    
    def __str__(self):
        return self.pcode
    
    class Meta:
        db_table='portinfo'