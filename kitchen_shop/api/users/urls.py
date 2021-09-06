from rest_framework import routers

from kitchen_shop.api.users.views import SessionViewSet

router = routers.DefaultRouter()
router.register('session', SessionViewSet, basename='session')

urlpatterns = router.urls
