
from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('',views.index, name='login'),
    path('signUp',views.signUp, name='signUp')
]