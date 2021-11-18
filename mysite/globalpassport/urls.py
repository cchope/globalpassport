from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('search/<str:code>', views.search_country),
    path('mypassport/ ', views.my_passport, name='myaccount'),


]
