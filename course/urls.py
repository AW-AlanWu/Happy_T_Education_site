from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('course/', views.course, name='course'),
    path('problem/', views.problem, name='problem'),
]