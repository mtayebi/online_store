from django.urls import path
from .apis import ProductView, ProductList
from .views import ProductHome

urlpatterns = [
    path('update/<int:pk>', ProductView.as_view(), name='product_view'),
    path('listview/', ProductList.as_view(), name='product_list'),
    path('', ProductHome.as_view(), name='home'),
]
