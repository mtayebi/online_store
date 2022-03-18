from django.shortcuts import render
from django.views import View
from product.models import Product


# Create your views here.
class ProductHome(View):
    def get(self, request):
        pros = Product.objects.all()
        context = {
            'pros': pros
        }
        return render(request, 'core/home.html', context=context)
