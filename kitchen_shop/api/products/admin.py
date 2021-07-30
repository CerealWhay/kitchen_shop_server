from django.contrib import admin

from kitchen_shop.api.products.models import Product, Category


admin.site.register(Product)
admin.site.register(Category)
