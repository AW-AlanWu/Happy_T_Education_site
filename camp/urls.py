from django.urls import path

from . import views

app_name = 'camp'

urlpatterns = [
    path('campList/', views.List, name='List'),
    path('campDetail/', views.Detail, name='Detail'),
    path('new/', views.new, name='new'),
    path('join/', views.join, name='join'),
]