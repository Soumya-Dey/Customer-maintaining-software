from django.shortcuts import render
from django.http import HttpResponse

# functions that return different views for different url routes
def home(request):
    return render(request, 'accounts/dashboard.html')

def products(request):
    return render(request, 'accounts/products.html')

def customer(request):
    return render(request, 'accounts/customer.html')
