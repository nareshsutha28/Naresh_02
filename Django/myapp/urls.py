from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name="index"),
    path('about/', views.about1, name="about"),
    path('login/', views.login, name="login"),

]