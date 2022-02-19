from django.urls import path
from .apis import ProductView, ProductList

urlpatterns = [
    path('update/<int:pk>', ProductView.as_view(), name='productview'),
    path('listview/', ProductList.as_view(), name='productlist')
]
