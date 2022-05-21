from django.urls import path, include
from .apis import ListCustomerAPI, ViewCustomerAPI, ViewAddressAPI, ListAddressAPI
from .views import CustomerLogin


app_name = 'customer'
api = [
    path('customerlist/', ListCustomerAPI.as_view(), name='customer_create_api'),
    path('customerupdate/<int:pk>', ViewCustomerAPI.as_view(), name='customer_update_api'),
    path('adresslist/', ListAddressAPI.as_view(), name='address_create_api'),
    path('adressupdate/<int:pk>', ViewAddressAPI.as_view(), name='address_update_api'),
]


urlpatterns = [
    path('api/', include(api), name='customer_api'),
    path('login/', CustomerLogin.as_view(), name='login'),
    # path('', profile.as_view(), name='profile'),
    ]
