from .models import Clients
from rest_framework import viewsets, permissions
from .serializers import ClientsSerializer

class ClientsViewSet(viewsets.ModelViewSet):
	queryset = Clients.objects.all()
	permission_classes = [permissions.AllowAny]
	serializer_class = ClientsSerializer

