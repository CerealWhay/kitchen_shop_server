from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from kitchen_shop.api.users import urls as users_urls
from kitchen_shop.docs import swagger_urls

schema_view = get_schema_view(
   openapi.Info(
      title="Kitchen_shop API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

api_urlpatterns = [
    path('users/', include(users_urls)),
]

urlpatterns = api_urlpatterns + swagger_urls()
