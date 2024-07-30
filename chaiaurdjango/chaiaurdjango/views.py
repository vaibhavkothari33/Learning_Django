# all the logic will be written here
# for the data base 
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, world You are at home page of the django server")

def about(request):
    return HttpResponse("Hello, world You are at about page of the django server")

def contact(request):
    return HttpResponse("Hello, world You are at contact page of the django server")

