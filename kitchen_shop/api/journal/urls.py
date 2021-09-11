from rest_framework import routers

from kitchen_shop.api.journal.views import (
    JournalViewSet,
)

router = routers.DefaultRouter()
router.register('', JournalViewSet, basename='journal')

urlpatterns = router.urls
