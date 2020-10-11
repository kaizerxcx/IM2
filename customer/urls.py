from django.urls import path
from . import views

#paths arranged alphabetically by name
app_name = 'customer'
urlpatterns = [
	# path('api/data', views.get_data, name='api-data'),

	#TEST URL
    path('main', views.MainIndexView.as_view(), name="main_view"),
    path('index', views.CustomerIndexView.as_view(), name="index_view"),
    path('CustomerRegistration', views.CustomerRegistrationView.as_view(), name="registration_view"),

] 


