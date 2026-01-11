from rest_framework import serializers


class SaleUpdateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=False)
    quantity = serializers.IntegerField(required=False)
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=False
    )
    date = serializers.DateField(required=False)


class SaleListSerializer(serializers.Serializer):
    month = serializers.CharField()
    quantity = serializers.IntegerField()
    profit = serializers.DecimalField(max_digits=10, decimal_places=2)
