from django.contrib import admin
from django.utils.safestring import mark_safe

from kitchen_shop.api.products.models import Product, Category

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'image_show',
        'description',
        'price',
        'stock',
        'created',
        'updated',
    ]

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='100' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Image"
