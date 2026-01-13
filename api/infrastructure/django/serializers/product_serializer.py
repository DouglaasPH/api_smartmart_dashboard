from rest_framework import serializers

from api.infrastructure.django.serializers.category_serializer import CategorySerializer


class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category_id = serializers.IntegerField()
    brand = serializers.CharField(max_length=100)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=300)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = CategorySerializer()
    brand = serializers.CharField(max_length=100)
