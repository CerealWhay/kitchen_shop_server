from rest_framework import serializers


class ProductPreviewSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)
    image = serializers.CharField(required=False)
    price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)


class ProductSerializer(serializers.Serializer):
    category = serializers.SlugRelatedField(required=False, slug_field='name', read_only=True)
    name = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)
    image = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    stock = serializers.IntegerField(required=False)
    created = serializers.DateTimeField(required=False)
    updated = serializers.DateTimeField(required=False)


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)
