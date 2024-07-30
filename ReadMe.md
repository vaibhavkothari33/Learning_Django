# Hello world

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