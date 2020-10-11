from django.contrib import admin
from django.urls import include,path
from . import views



app_name = 'dvdReports'
urlpatterns = [
  #  path
    path('index', views.dvdReportsView.as_view(), name="index_view"),
    # path('dvdReportSuccesUpdate', views.dvdReportSuccesUpdateView.as_view(), name="dvdReportSuccesUpdate"),
]
