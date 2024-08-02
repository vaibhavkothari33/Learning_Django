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

### also never forget about the static folder and the template folder 
``` py
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