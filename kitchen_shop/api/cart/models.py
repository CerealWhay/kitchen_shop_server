from django.db import models

from kitchen_shop.api.products.models import Product
from kitchen_shop.api.users.models import Customer


class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer


class CartProduct(models.Model):
    order = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product} from cart"
