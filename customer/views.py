from django.shortcuts import render,redirect
from django.views import View
from product.models import Product
from customer.forms import CustomerForm, UserForm
from core.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.
class CustomerLogin(View):

    def get(self, request):
        if request.user.is_authenticated:
            pros = Product.objects.all()
            context = {
            'pros': pros
             }
            return render(request, 'core/home.html', context=context)
        else:
            form = UserForm()
            return render(request, 'customer/login.html', {'form':form})


    def post(self,request):
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(phone = phone, password=password)
        if user:
            login(request, user)
            return redirect('/product')
        else:
            return redirect('customer:login')



class CustomerSignup(View):
    def get(self, request):
        if request.user.is_authenticated:
            pros = Product.objects.all()
            context = {
            'pros': pros
             }
            return render(request, 'core/home.html', context=context)
        else:
            customerform = CustomerForm()
            userform = UserForm()
            return render(request, 'customer/signup.html', {'customerform':customerform, 'userform':userform})


    def post(self, request):
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = User.objects.create_user(phone=phone, password=password)
        login(request, user)
        return redirect('/product')


class CustomerLogout(View):

    def get(self, request):
        logout(request)
        return redirect('/product')






