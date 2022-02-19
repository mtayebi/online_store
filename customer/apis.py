from rest_framework import generics
from customer.serilizers import CustomerSerializer, AddressSerializer
from customer.models import Customer, Address


class ListCustomerAPI(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ViewCustomerAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
