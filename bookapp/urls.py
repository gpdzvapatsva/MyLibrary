
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.readers, name='readers'),
    path('books/', views.mybooks, name='books')
]
