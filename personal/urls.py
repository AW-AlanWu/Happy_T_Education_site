from django.urls import path

from . import views

app_name = 'personal'

urlpatterns = [
    path('', views.userProfile, name='userProfile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/saveAccount/', views.saveAccount, name='saveAccount'),
    path('login/authenticateAccount/', views.authenticateAccount, name='authenticateAccount'),
    path('log_out/', views.log_out, name='log_out'),
]