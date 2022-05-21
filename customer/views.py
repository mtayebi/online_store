from django.shortcuts import render
from django.views import View
from product.models import Product


class CustomerLogin(View):

    def get(self, request):
        if request.user.is_authenticated:
            pros = Product.objects.all()
            context = {
            'pros': pros
             }
            return render(request, 'core/home.html', context=context)
        else:
            return render(request, 'customer/login.html')
