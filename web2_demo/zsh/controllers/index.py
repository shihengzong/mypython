from django.http import HttpResponse, JsonResponse
from django.core import serializers 
import json

import sys,os
from zsh import models

def index(request):
    p = models.Person(p_name='LiLei', p_age=20, p_sex=False)
    p.save() # 插入
    return HttpResponse("this is a page about index !")

def list(request):
    persons =  models.Person.objects.all()# 查询
    list_str = serializers.serialize("json",persons) # 序列化成
    dict_persons = json.loads(list_str)
    p = persons[0]
    # 更新
    p.p_name = 'HanMeiMei'
    p.save()
    return JsonResponse(list_str,safe=False)
    
def filter(request):
    # exclude (!=)  filter(=)
    persons = models.Person.objects.all().exclude(p_name="Jane").filter(p_age="18")
    list_str = serializers.serialize("json",persons) 
    print("type:",type(persons))
    return JsonResponse(list_str,safe=False)

def test_val(request):
    # exclude (!=)  filter(=)
    persons = models.Person.objects.all()
    list_str = serializers.serialize("json",persons) 
    print("type:"+"="*30,type(persons))
    print("%s\n" % list_str)
    return JsonResponse(list_str,safe=False)