from django.db import models
from .logic.image_filepath import product_image_path


class Product(models.Model):

    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default='slug_product')
    image = models.ImageField(upload_to=product_image_path, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default='slug_category')

    def __str__(self):
        return self.name
