from django.http import HttpResponse
from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404

from kitchen_shop.api.products.models import Product, Category
from kitchen_shop.api.products.serializers import (
    CategorySerializer,
    ProductSerializer,
)


class CategoriesViewSet(ViewSet):
    permission_classes = (permissions.AllowAny,)

    @action(methods=('get',), detail=False)
    def get_categories(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        response = serializer.data
        return Response(
            data=response, status=status.HTTP_200_OK,
        )


class ProductsViewSet(ViewSet):
    permission_classes = (permissions.AllowAny,)

    @action(methods=('post',), detail=False)
    def get_products(self, request):
        if request.data.get('category_slug'):
            category = get_object_or_404(Category, slug=request.data.get('category_slug'))
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        response = serializer.data
        return Response(
            data=response, status=status.HTTP_200_OK
        )

    @action(methods=('post',), detail=False)
    def get_selected_product(self, request):
        product = get_object_or_404(Product, slug=request.data.get('slug'))
        serializer = ProductSerializer(product)
        response = serializer.data

        return Response(
            data=response, status=status.HTTP_200_OK
        )

    @action(methods=('post',), detail=False)
    def search_products(self, request):
        products = Product.objects.filter(name__icontains=request.data.get('text'))
        serializer = ProductSerializer(products, many=True)
        response = serializer.data
        return Response(
            data=response, status=status.HTTP_200_OK
        )
