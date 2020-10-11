from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from dashboard.models import DVD, Cast, Images
from customer.models import Customer
from order.models import Order


# Create your views here.



class orderView(View):
	def get(self, request):
		dvds = DVD.objects.all()		
		images = Images.objects.all()
		customers = Customer.objects.all()
		orders = Order.objects.all()
		orderTable = Order.objects.raw("select `order`.order_date, `order`.employee_id_id as id, sum(price) as total from `order` JOIN `dvd` ON `order`.sku = `dvd`.sku  GROUP BY `order`.employee_id_id")
		context={
			'dvds' : dvds,
			'images': images,
			'customers':customers,
			'orders': orders,
			'orderTable': orderTable, 
		}
		return render(request,'order/index.html', context)
	def post(self, request):
		if request.method == 'POST':
			if 'btnUpdate' in request.POST:
				employee_id = request.POST.get("customerInfo")
				update_order = Order.objects.filter(employee_id_id= employee_id).delete()
				for order in request.POST.getlist('orderInfos[]'):
					orders = Order.objects.create(employee_id_id=employee_id, sku = order)

			elif 'btnDelete' in request.POST:
				employee_id = request.POST.get("deleteInfo")
				delete_order = Order.objects.filter(employee_id_id= employee_id).delete()

			else:
				return HttpResponse('not valid') 
				
		return redirect('order:index_view')