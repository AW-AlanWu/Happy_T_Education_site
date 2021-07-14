from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('course/', views.course, name='course'),
    path('problem/', views.problem, name='problem'),
    path('new/', views.new, name='new'),
    path('detail/', views.detail, name='detail'),
    path('detail/check/', views.check, name='check'),
]