from django.urls import path
from . import views
#http://127.0.0.1:8000/

urlpatterns = [
    path("", views.login_request, name='login_request'),
    path("login", views.login_request, name='login_request'),
    path("signup", views.signup_request, name = 'signup'),
    path("forgotpass", views.forgotpass_request, name='forgotpass'),
    path('profil', views.profil, name='profil'),
]