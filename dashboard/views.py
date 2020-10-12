from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .forms import DVDForm
from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
# from dvdReports.urls import *
# Create your views here.


class welcomeView(View):
	def get(self, request):
		# dvds = DVD.objects.all()
		# for dvd in dvds:
		# 	print(dvd.title)
		return render(request,'dashboard/landingPage.html')

class loginfailView(View):
	def get(self, request):
		# dvds = DVD.objects.all()
		# for dvd in dvds:
		# 	print(dvd.title)
		return render(request,'dashboard/SignInFailed.html')	
		
class dashboardView(View):
	def get(self, request):
		# dvds = DVD.objects.all()
		# for dvd in dvds:
		# 	print(dvd.title)
		return render(request,'dashboard/dashboard.html')
	#def post(self, request):
	#	if request.method == 'POST':
		#	return render(request,'CSIT327/dvdReport.html') 

class dashboardDVDRegisterView(View):
	"""docstring for dashboardDVDRegisterView"""
	def get(self, request):
		return render(request,'dashboard/dvdRegistration.html')
	def post(self, request):
		form = DVDForm(request.POST)
		if form.is_valid():

			sku = request.POST.get("sku")
			date_registered = request.POST.get("date_registered")
			genre = request.POST.get("Genre")
			title = request.POST.get("title")
			released_date = request.POST.get("released_date")
			director = request.POST.get("director")
			price = request.POST.get("price")
			items  =  request.POST.get("items")

			form = DVD(sku = sku, date_registered = date_registered, genre = genre, title = title, 
						released_date = released_date, director = director, price = price, items = items)

			form.save()
			
			for cast in request.POST.getlist('cast[]'):
				dvdSKU = DVD.objects.get(sku=sku)
				cast = Cast.objects.create(sku= dvdSKU, fullname = cast)
				print(cast.fullname)

			for image in request.FILES.getlist('files[]'):
				fs = FileSystemStorage()
				filename = fs.save(image.name, image)
				imgSKU = DVD.objects.get(sku=sku)
				Images.objects.create(sku = imgSKU, link="/media/"+filename)

		
			
			return redirect('dvdReports:index_view')
		else:
			print(form.errors)
			return HttpResponse('not valid')
			