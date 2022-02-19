from rest_framework import generics
from order.models import OrderItem,DiscountCode, Basket
from .serializers import OrderItemSerializer, DiscountCodeSerializer, BasketSerializer


class ViewOrderItemAPI(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class ListOrderItemAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class ViewBasketAPI(generics.ListCreateAPIView):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()


class ListBasketAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()


class ListDiscountCodeAPI(generics.ListCreateAPIView):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()


class ViewDiscountCodeAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiscountCodeSerializer
    queryset = DiscountCode.objects.all()