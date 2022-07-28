from django.urls import path
from .import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('register/', views.registerfun, name = 'register'),
    path('login_to', views.login_to, name="login_to"),
    path('index/', views.index, name = 'index'),
]