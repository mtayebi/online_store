from django.urls import path
from .apis import *

urlpatterns=[
    path('orderitemlistapi/', ListOrderItemAPI.as_view(), name='order_item_list_api'),
    path('orderitemviewapi/', ViewOrderItemAPI.as_view(), name='order_item_view_api'),
    path('basketlistapi/', ListBasketAPI.as_view(), name='basket_list_api'),
    path('basketviewapi/', ViewBasketAPI.as_view(), name='basket_view_api'),
    path('discountlistapi/', ListDiscountCodeAPI.as_view(), name='Discount_code_list_api'),
    path('discountviewapi/', ViewDiscountCodeAPI.as_view(), name='Discount_code_view_api'),
]