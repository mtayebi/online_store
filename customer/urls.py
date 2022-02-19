from django.urls import path
from .apis import ListCustomerAPI,ViewCustomerAPI

urlpatterns = [
    path('customerlist/', ListCustomerAPI.as_view(), name='customer_create_api'),
    path('customerupdate/<int:pk>', ViewCustomerAPI.as_view(), name='customer_update_api'),
]
