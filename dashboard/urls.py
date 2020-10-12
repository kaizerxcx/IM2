from django.contrib import admin
from django.urls import include,path
from . import views



app_name = 'dashboard'
urlpatterns = [
  #  path
    path('welcome', views.welcomeView.as_view(), name="welcome_view"),
    path('loginfail', views.loginfailView.as_view(), name="loginfail_view"),
    path('index', views.dashboardView.as_view(), name="index_view"),
    path('dvdRegistration', views.dashboardDVDRegisterView.as_view(), name="dvdRegistration_view"),
   

]
