from django.urls import path
from .apis import ListCustomerAPI, ViewCustomerAPI, ViewAddressAPI, ListAddressAPI


urlpatterns = [
    path('customerlist/', ListCustomerAPI.as_view(), name='customer_create_api'),
    path('customerupdate/<int:pk>', ViewCustomerAPI.as_view(), name='customer_update_api'),
    path('adresslist/', ListAddressAPI.as_view(), name='address_create_api'),
    path('adressupdate/<int:pk>', ViewAddressAPI.as_view(), name='address_update_api'),
]
