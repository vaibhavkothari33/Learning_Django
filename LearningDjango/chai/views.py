from django.shortcuts import render

# Create your views here.
def all_chai(request):
    return render(request,"chai/all_chai.html")
def all_orders(request):
    return render(request,"chai/Orders.html")