from django.shortcuts import render
from django.http import Http404
from .models import Bank
from django.http import JsonResponse
from django.core import serializers
import json
from django.http import HttpResponse

def detail(request, ifsc):
    try:
        p = Bank.objects.filter(ifsc=ifsc)
        
        print(p)
        posts_serialized = serializers.serialize('json', p)
    except Bank.DoesNotExist:
        raise Http404("Poll does not exist")
    
    return HttpResponse(json.dumps(posts_serialized), content_type="application/json")

def bankDetail(request, city, name):
    print(city)
    print(name)
    try:
        p = Bank.objects.filter(city=city)
        p1 = p.filter(name=name)
        print(p)
        posts_serialized = serializers.serialize('json', p1)
    except Bank.DoesNotExist:
        raise Http404("Poll does not exist")
    
    return HttpResponse(json.dumps(posts_serialized), content_type="application/json")

