from rest_framework import serializers
from .models import Clients

class ClientsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Clients
		fields = ('id', 'name', 'number', 'date_info', 'description')
		read_only_fields = ('date_info', )
