from django.contrib import admin
from django.urls import path ,include
from . import views


urlpatterns = [
    
    path('api/<int:ifsc>/', views.detail, name='post_detail'),
    path('api/<str:city>/<str:name>/', views.bankDetail, name = 'bankDetail')
] 
