from rest_framework import serializers


class CartProductSerializer(serializers.Serializer):
    product_slug = serializers.CharField(required=False)
    quantity = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    total_price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
