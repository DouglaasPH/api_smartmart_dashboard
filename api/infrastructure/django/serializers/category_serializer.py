# infrastructure/api/serializers.py
from rest_framework import serializers


class CategoryCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
