from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# functions that return different views for different url routes
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    order_delivered = orders.filter(status = 'Delivered')
    order_pending = orders.filter(status = 'Pending')

    context = {
        'customers': customers,
        'orders': orders,
        'totalOrders': orders.count(),
        'totalCustomers': customers.count(),
        'deliveredCount': order_delivered.count(),
        'pendingCount': order_pending.count()
    }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'accounts/products.html', context)

def customer(request, pk):
    customer = Customer.objects.get(id=int(pk))
    orders = customer.order_set.all()

    context = {
        'customer': customer,
        'orders': orders,
        'orderCount': orders.count()
    }
    return render(request, 'accounts/customer.html', context)
