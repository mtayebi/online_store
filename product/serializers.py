from rest_framework import serializers
from .models import Product, Category


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     pro_name = serializers.CharField(max_length=40)
#     price = serializers.IntegerField()
#     brand = serializers.CharField()
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     create_time = serializers.DateTimeField(read_only=True)
#
#     def update(self, instance: Product, validated_data:dict) -> Product:
#         instance.pro_name = validated_data.get('pro_name', instance.pro_name)
#         instance.price = validated_data.get('price', instance.price)
#         instance.brand = validated_data.get('brand', instance.brand)
#         instance.category = validated_data.get('category', instance.category)
#         return instance
#
#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

