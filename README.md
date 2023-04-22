# django-rest-framework-crud
working with django rest framework


## Commands

```
pipenv shell
pipenv install django 
pipenv install djangorestframework
python manage.py createproject crudproject .
python manage.py startapp crudapp1
```

## Install the app and the djangorestframework

- To the file `crudproject/settings.py` add, the `crudapp` and the `rest_framework`
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

## Created the model

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

