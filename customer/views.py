from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from .forms import CustomerForm
from .models import *
from django.core.files.storage import FileSystemStorage
from dashboard.models import DVD, Cast, Images
from order.models import Order

# Create your views here.


class CustomerIndexView(View):
    def get(self, request):
        customers = Customer.objects.all()
        dvds = DVD.objects.all()
        cast =  Cast.objects.all()
        images = Images.objects.all()

        context = {
            'customers' : customers,
            'dvds' : dvds,
            'casts': cast,
            'images': images,
        }
        return render(request, 'customer/index.html', context)
    def post(self, request):
        if request.method == 'POST':

            if 'btnUpdate' in request.POST:
                employee_id = request.POST.get("employee_id")
                date_registered = request.POST.get("date_registered")
                fname = request.POST.get("firstname")
                mname = request.POST.get("middlename")
                lname = request.POST.get("lastname")
                address = request.POST.get("address")
                birthdate = request.POST.get("birthdate")
                gender = request.POST.get("gender")
                status = request.POST.get("status")
                spouse_name = request.POST.get("spouse_name")
                spouse_occupation = request.POST.get("spouse_occupation")
                children = request.POST.get("children")

                path = ""
                for profile_pic in request.FILES.getlist('profile_pic[]'):
                    fs = FileSystemStorage()
                    path = fs.save(profile_pic.name, profile_pic)

                form = Customer.objects.filter(employee_id = employee_id).update(date_registered = date_registered, firstname = fname, middlename = mname, 
                                        lastname = lname, address =address,
                                      birthdate = birthdate,  gender = gender, status = status, 
                                      spouse_name = spouse_name , spouse_occupation = spouse_occupation,
                                      children = children, profile_pic ="/media/"+path)
                
            elif 'btnDelete' in request.POST:
                employee_id = request.POST.get("deleteInfo")
                delete_customer = Customer.objects.filter(employee_id= employee_id).delete()
                delete_person = Person.objects.filter(employee_id= employee_id).delete()

            elif 'btnOrder'in request.POST:
                employee_id = request.POST.get("customerInfo")
                for order in request.POST.getlist('orderInfos[]'):
                    emp_id = Customer.objects.get(person_ptr =  employee_id)
                    print(order)
                    orders = Order.objects.create(employee_id =  emp_id, sku = order)
                return redirect('order:index_view')
         
            else:
              
                return HttpResponse('not valid')    

        return redirect('customer:index_view')


class CustomerRegistrationView(View):
    def get(self, request):
    	# print('get')
    	return render(request, 'customer/registration.html')

    def post(self, request):
        form = CustomerForm(request.POST)
        # fname = request.POST.get("firstname")
        # print(fname)
        # lname = request.POST.get("lastname")
        # print(lname)
        if request.method == 'POST':
            # try:
            if form.is_valid():
              
                date_registered = request.POST.get("date_registered")
                fname = request.POST.get("firstname")
                mname = request.POST.get("middlename")
                lname = request.POST.get("lastname")
                address = request.POST.get("address")
                birthdate = request.POST.get("birthdate")
                gender = request.POST.get("gender")
                status = request.POST.get("status")
                spouse_name = request.POST.get("spouse_name")
                spouse_occupation = request.POST.get("spouse_occupation")
                children = request.POST.get("children")
                path = ""
                for profile_pic in request.FILES.getlist('profile_pic'):
                    fs = FileSystemStorage()
                    path = fs.save(profile_pic.name, profile_pic)

                
                form = Customer(date_registered = date_registered, firstname = fname, middlename = mname, 
                                        lastname = lname, address =address,
                                      birthdate = birthdate,  gender = gender, status = status, 
                                      spouse_name = spouse_name , spouse_occupation = spouse_occupation,
                                      children = children, profile_pic ="/media/"+path)
                form.save()

                return redirect('customer:index_view')
           

            else:
                print(form.errors)
                return HttpResponse('not valid')   	

   