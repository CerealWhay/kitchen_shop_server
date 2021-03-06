from django.urls import path, include
from kitchen_shop.api.users import urls as users_urls
from kitchen_shop.api.products import urls as products_urls
from kitchen_shop.api.cart import urls as cart_urls
from kitchen_shop.api.journal import urls as journal_urls


urlpatterns = [
   path('users/', include(users_urls)),
   path('products/', include(products_urls)),
   path('cart/', include(cart_urls)),
   path('journal/', include(journal_urls)),
]
