from rest_framework import routers
from .api import ClientsViewSet, TestViewSet

router = routers.DefaultRouter()

router.register('api/clients', ClientsViewSet, 'clients')
router.register('api/test1', TestViewSet, 'test1')

urlpatterns = router.urls
