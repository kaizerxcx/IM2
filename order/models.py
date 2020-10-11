from django.db import models
from customer.models import Customer
from datetime import datetime
from django.utils import timezone
# Create your models here.




class Order(models.Model):
	order_date = models.DateField(default = datetime.now())
	employee_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	sku = models.CharField(max_length=255, default = "10101")
	class Meta:
		db_table = "Order"