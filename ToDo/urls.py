from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path("todo/", views.index, name="index"),
    path('registration/', views.registration, name="registration"),
    path('submit/',views.submit, name="submit"),
    path('login/',views.login, name="login")
]