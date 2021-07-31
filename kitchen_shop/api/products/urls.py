from rest_framework import routers

from kitchen_shop.api.products.views import (
    ProductsViewSet,
    CategoriesViewSet,
)

router = routers.DefaultRouter()
router.register('products', ProductsViewSet, basename='products')
router.register('categories', CategoriesViewSet, basename='categories')

urlpatterns = router.urls
