from django.urls import path
from .import views

urlpatterns = [
    path("",views.all_chai,name="all_home"),
    path("orders/",views.all_chai,name="Orders"),
]
