from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.



# class Cast(models.Model):
# 	# sku = models.ForeignKey(DVD, on_delete=models.CASCADE)
# 	firstname = models.CharField(max_length=500, default = "ddd")
# 	lastname = models.CharField(max_length=500, default = "ddd")

# 	class Meta:
# 		db_table = "Cast"




class DVD(models.Model):
	sku = models.CharField(max_length=255, primary_key=True, default = "10101")
	date_registered = models.DateField(default = datetime.now())
	genre = models.CharField(max_length=1000)
	title = models.CharField(max_length=350)
	released_date = models.DateField(default = datetime.now())
	director = models.CharField(max_length=255)
	price = models.FloatField(default = 0.00)
	items = models.IntegerField(default = 0)
	
	class Meta:
		db_table = "DVD"



class Cast(models.Model):
	sku = models.ForeignKey(DVD,null=True, blank=False, unique=False,  on_delete=models.CASCADE)
	fullname = models.CharField(max_length=500)


	class Meta:
		db_table = "Cast"
	


class Images(models.Model):
	sku = models.ForeignKey(DVD, on_delete=models.CASCADE)
	link = models.FileField()

	class Meta:
		db_table = "Images"

