from django.contrib import admin
from django.urls import include,path
from . import views


app_name = 'order'
urlpatterns = [
  #  path
    path('index', views.orderView.as_view(), name="index_view"),
   

]
