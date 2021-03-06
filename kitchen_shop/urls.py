from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from kitchen_shop.api import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('tinymce/', include('tinymce.urls')),
    path('api/v1/', include(api_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
