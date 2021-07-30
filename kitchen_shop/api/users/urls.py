from rest_framework import routers

from kitchen_shop.api.users.views import BaseAuthViewSet, UserDataViewSet

router = routers.DefaultRouter()
router.register('auth/base', BaseAuthViewSet, basename='auth_base')
router.register('user_data', UserDataViewSet, basename='user_data')

urlpatterns = router.urls
