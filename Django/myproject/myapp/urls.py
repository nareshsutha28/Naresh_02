from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name="index"),
    path('about/', views.about1, name="about"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('contact/', views.contact, name="contact"),
    path('logout/', views.logout, name="logout"),
    path('change/', views.change_pas, name="change_pas"),
    path('profile/', views.profile, name="profile"),
    path('profile/', views.profile, name="profile"),
    path('forget/', views.forget_pas, name="forget_pas"),
    path('varify_otp/', views.enter_otp, name="enter_otp"),
    path('new_pas/', views.new_pas, name="new_pas"),
    
       

]
