from django.contrib import admin
from django.urls import path,re_path
from SuperApp import views as da

urlpatterns = [
    path("",da.HomePage),
]