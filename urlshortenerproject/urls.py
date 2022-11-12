from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.signUp, name='sign-up'),
    path('log-in/', views.logIn, name='log-in'),
    path('create-url-shortener/', views.create_url_shortener, name='create-url-shortener'),
    path('invalid-token/', views.unauthorized, name='invalid-token'),
    path('<str:shortened_part>/', views.redirect_url_view, name='redirect'),
    
]