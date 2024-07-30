# all the logic will be written here
# for the data base 
from django.http import HttpResponse
from django.shortcuts import render;
def home(request):
    # return HttpResponse("Hello, world You are at home page of the django server")
    return render(request,'website/index.html')

def about(request):
    # return HttpResponse("Hello, world You are at about page of the django server")
    return render(request,'website/about.html')

def contact(request):
    # return HttpResponse("Hello, world You are at contact page of the django server")
    return render(request,'website/contact.html')

