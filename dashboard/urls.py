from django.contrib import admin
from django.urls import include,path
from . import views



app_name = 'dashboard'
urlpatterns = [
  #  path
    path('index', views.dashboardView.as_view(), name="index_view"),
    path('dvdRegistration', views.dashboardDVDRegisterView.as_view(), name="dvdRegistration_view"),
   

]
