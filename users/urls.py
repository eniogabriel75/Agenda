from django.urls import path
from . import views

urlpatterns = [
     path('', views.login, name = 'login'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('validate/', views.validate, name='validate'),
    path('validateLogin/', views.validateLogin, name='validateLogin'),
    path('recover/', views.recover, name='recover'),
    path('validateRecover/', views.validateRecover, name='validateRecover'),
    path('leave/', views.leave, name ='leave'),
]