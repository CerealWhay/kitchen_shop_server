from rest_framework import routers

from kitchen_shop.api.users.views import BaseAuthViewSet

router = routers.DefaultRouter()
router.register('auth/base', BaseAuthViewSet, basename='auth_base')

urlpatterns = router.urls
