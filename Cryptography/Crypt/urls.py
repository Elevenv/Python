from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('',views.ui,name="ui"),
    path('Encrypt/',views.Encrypt),
    path('Decrypt/',views.Decrypt),
]
