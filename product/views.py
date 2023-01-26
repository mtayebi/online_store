from django.shortcuts import render, HttpResponse
from django.views import View
from product.models import Product
from json import loads

# Create your views here.
class ProductHome(View):
    def get(self, request):
        pros = Product.objects.all()
        context = {
            'pros': pros
        }
        return render(request, 'core/home.html', context=context)


class Purchase(View):

    def get(self, request):
        if request.COOKIES.get('orders', None):
            orders = loads(request.COOKIES.get('orders'))
            temp = {}
            for item, number in orders.items():
                temp[Product.objects.get(id=item)] = number
            context = {
                "orders": temp
            }
            return render(request, 'core/purchase.html', context=context)
        else:
            return render(request, 'core/empty_basket.html')

