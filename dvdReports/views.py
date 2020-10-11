from django.shortcuts import render
from django.views.generic import View, TemplateView
# Create your views here.
from dashboard.models import DVD, Cast, Images
from dashboard.forms import DVDForm
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

class dvdReportsView(View):
	def get(self, request):
		dvds = DVD.objects.all()
		# for dvd in dvds:
		# 	cast = Cast.objects.filter(sku = dvd.sku)
		cast =  Cast.objects.all()
		
		images = Images.objects.all()
		# for dvd in dvds:
		# 	print(dvd.title)
		context={
			'dvds' : dvds,
			'casts': cast,
			'images': images,
		}
		return render(request,'dvdReports/dvdReport.html', context)
	
	def post(self, request):
		if request.method == 'POST':

			if 'btnUpdate' in request.POST:
				sku = request.POST.get("sku")
				date_registered = request.POST.get("date_registered")
				genre = request.POST.get("Genre")
				title = request.POST.get("title")
				released_date = request.POST.get("released_date")
				director = request.POST.get("director")
				price = request.POST.get("price")
				items  =  request.POST.get("items")

				update_dvd = DVD.objects.filter(sku = sku).update(date_registered = date_registered, genre = genre, title = title, 
							released_date = released_date, director = director, price = price, items = items)
				
				update_cast = Cast.objects.filter(sku = sku).delete()

				for cast in request.POST.getlist('cast[]'):
					dvdSKU = DVD.objects.get(sku=sku)
					cast = Cast.objects.create(sku= dvdSKU, fullname = cast)


				# for image in request.POST.getlist('imageLink[]'):
				# 	fs = FileSystemStorage()
				# 	filename = fs.delete(image.replace("/media/", ''))
	
				update_images = Images.objects.filter(sku = sku).delete()

				for image in request.FILES.getlist('fileses'):
					fs = FileSystemStorage()
					filename = fs.save(image.name, image)
					imgSKU = DVD.objects.get(sku=sku)
					Images.objects.create(sku = imgSKU, link="/media/"+filename)
					print(filename);

				for img in request.POST.getlist('imageLink[]'):
					imgSKU = DVD.objects.get(sku=sku)
					image = Images.objects.create(sku= imgSKU, link = img)
					
				
			elif 'btnDelete' in request.POST:
				print('delete button clicked')
				print('delete button clicked')
				print('delete button clicked')
				skuss = request.POST.get("deleteInfo")
				delete_cast = Cast.objects.filter(sku = skuss).delete()
				delete_images = Images.objects.filter(sku = skuss).delete()
				delete_dvd = DVD.objects.filter(sku = skuss).delete()	


		return redirect('dvdReports:index_view')
				# return redirect('dvdReports:index_view')



# class dvdReportsView(View):