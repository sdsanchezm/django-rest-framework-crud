from rest_framework import routers
from .api import ClientsViewSet

router = routers.DefaultRouter()

router.register('api/clients', ClientsViewSet, 'clients')

urlpatterns = router.urls