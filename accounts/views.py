from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

# functions that return different views for different url routes
def home(request):
    # fetching data from the database models
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

    # rendering the page
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    # fetching data from the database models
    products = Product.objects.all()

    context = {
        'products': products
    }

    # rendering the page
    return render(request, 'accounts/products.html', context)

def customer(request, pk):
    # fetching data from the database models
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all()

    context = {
        'customer': customer,
        'orders': orders,
        'orderCount': orders.count()
    }

    # rendering the page
    return render(request, 'accounts/customer.html', context)

def createOrder(request):
    form = OrderForm()
    
    # if request is POST i.e submit button is clicked then
    # saving the form to the database
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()

            # method to redirect to the dashboard page
            return redirect('/')

    context = {'form': form}

    # rendering the page
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id = pk)
    form = OrderForm(instance = order)

    # if request is POST i.e submit button is clicked then
    # saving the form to the database
    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order)

        if form.is_valid():
            form.save()

            # method to redirect to the dashboard page
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id = pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {
        'item': order
    }

    return render(request, 'accounts/delete.html', context)