from rest_framework import routers

from kitchen_shop.api.cart.views import (
    CartViewSet,
)

router = routers.DefaultRouter()
router.register('cart', CartViewSet, basename='cart')

urlpatterns = router.urls
