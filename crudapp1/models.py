from django.db import models

# Create your models here.

class Clients(models.Model):
	name = models.CharField(max_length=200)
	number = models.IntegerField()
	date_info = models.DateTimeField(auto_now_add=True)
	description = models.TextField()