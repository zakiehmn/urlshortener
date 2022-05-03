from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.signUp, name='sign-up'),
    path('log-in/', views.logIn, name='log-in'),
]