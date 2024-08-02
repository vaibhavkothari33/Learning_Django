# Hello world
### install the uv
```py
pip install uv
```
### Then locate this 
```
.venv\Scripts\activate
```
### install Django
```py
uv pip install Django
```
### make the project
```py
django-admin startproject name_of_the_project
```
```py
django-admin startproject LearingDjango
```
### Cd into that folder then run

```py 
python .\manage.py runserver
```

## few important changes to be made is in setting to load html css and js and views for routes 

### make the views.py file
```py
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world")
    return render(request,"website/index.html")
def about(request):
    # return HttpResponse("Hello world")
    return render(request,"website/about.html")
def contact(request):
    # return HttpResponse("Hello world")
    return render(request,"website/contact.html")
```
#
### also never forget about the static folder and the template folder 
``` py
import os
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,"static")]
```

### changes in url file for the routes
```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
]
```
```html
{% load static %}
<link rel="stylesheet" href="{%static 'style.css'%}">

```
### When we make a new app using 
```powershell
python .\manage.py startapp chai
```
### Aware the whole app about the new app

### go in the setting of the learnig django and 
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chai', # add the new file /app name
]
```
### handling the urls of the different app 
```py
from django.contrib import admin
from django.urls import path ,include ####
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path("chai/",include("chai.urls")), ###
]
```