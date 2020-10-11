from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.

class Person(models.Model):
	employee_id = models.AutoField(primary_key=True)
	firstname = models.CharField(max_length = 100)
	middlename = models.CharField(max_length = 100, default="NA")
	lastname = models.CharField(max_length = 100)
	address = models.CharField(max_length = 355)
	birthdate = models.DateField(default = datetime.now())
	status = models.CharField(max_length = 50)
	gender = models.CharField(max_length = 50)
	spouse_name = models.CharField(max_length = 700, default="None")
	spouse_occupation = models.CharField(max_length = 500, default="None")
	children = models.IntegerField(default=0)
	class Meta:
		db_table = "Person"

class Customer(Person):
	date_registered =models.DateField(default = datetime.now())
	profile_pic = models.FileField()
	class Meta:				
		db_table = "Customer"
