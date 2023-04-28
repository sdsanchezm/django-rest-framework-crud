# django-rest-framework-crud
working with django rest framework


## Install the app and the djangorestframework and initialize the shell

```
pipenv shell
pipenv install django 
pipenv install djangorestframework
python manage.py createproject project1 .
python manage.py startapp app1
```

- To the file `crudproject/settings.py` add, the `crudapp1` and the `rest_framework`
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crudapp1', 
    'rest_framework',
]
```

## Create the model https://www.django-rest-framework.org/api-guide/viewsets/

```
from django.db import models

# Create your models here.

class Clients(models.Model):
	name = models.CharField(max_length=200)
	number = models.IntegerField()
	date_info = models.DateTimeField(auto_now_add=True)
	description = models.TextField()
```

## Make migrations and migrate

```
python manage.py makemigrations
python manage.py migrate
```

## Create the `crudapp1/urls.py` file

```
from rest_framework import routers
from .api import StudentViewSet
# from django.http import HttpResponse

router = routers.DefaultRouter()

router.register('api/students', StudentViewSet, 'students')

urlpatterns = router.urls
```

## Create the `api.py` file and include the `ViewSet`

```
from .models import Student
from rest_framework import viewsets, permissions
from .serializers import StudentsSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentsSerializer

```

- Documentation at [https://www.django-rest-framework.org/api-guide/viewsets/](https://www.django-rest-framework.org/api-guide/viewsets/)
    - Options for view sets:
        - viewsets.ViewSet
        - viewsets.ModelViewSet
        - viewsets.ReadOnlyModelViewSet


## Create the `serializers.py` file 

```
from rest_framework import serializers
from .models import Student

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        kk1 = 5454
        fields = ('id', 'name', 'number', 'date_info')
#       read_only_fields = ('date_info', )

```

- Documentation: [https://www.django-rest-framework.org/api-guide/serializers/](https://www.django-rest-framework.org/api-guide/serializers/)
    - 
