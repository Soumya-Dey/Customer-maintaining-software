from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import OrderForm, RegisterUserForm
from .filters import OrderFilter

# functions that return different views for different url routes
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegisterUserForm()

        if request.method == 'POST':
            form = RegisterUserForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, 'Account successfully created for ' + form.cleaned_data.get('username'))

                return redirect('login')

        context = {
            'form': form
        }

        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            # if the user is in registered list
            if user is not None:
                login(request, user)

                return redirect('home')
            else:
                messages.error(request, 'username or password incorrect')

        context = {}

        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# login in required to view these pages
# if not logged in then the user id redirected to the login page
@login_required(login_url='login') 
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

# login in required to view these pages
# if not logged in then the user id redirected to the login page
@login_required(login_url='login') 
def products(request):
    # fetching data from the database models
    products = Product.objects.all()

    context = {
        'products': products
    }

    # rendering the page
    return render(request, 'accounts/products.html', context)

# login in required to view these pages
# if not logged in then the user id redirected to the login page
@login_required(login_url='login') 
def customer(request, pk):
    # fetching data from the database models
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all()

    filters = OrderFilter(request.GET, queryset = orders)
    orders = filters.qs

    context = {
        'customer': customer,
        'orders': orders,
        'orderCount': orders.count(),
        'filters': filters
    }

    # rendering the page
    return render(request, 'accounts/customer.html', context)

# login in required to view these pages
# if not logged in then the user id redirected to the login page
@login_required(login_url='login') 
def createOrder(request, pk):
    customer = Customer.objects.get(id = pk)
    # setting the instance of the form to the current order
    # 'initial' is for setting only one option
    # form = OrderForm(initial = {
    #     'customer': customer
    # })

    OrderFormSet = inlineformset_factory(Customer, Order, fields = ('product', 'status'), extra = 2)
    # queryset = Order.objects.none() is for only showing the options for new orders i.e hiding the current orders
    # setting the instance of the form to the current order
    # 'instance' is for setting all options at once
    formset = OrderFormSet(queryset = Order.objects.none(), instance = customer)
    
    # if request is POST i.e submit button is clicked then
    # saving the form to the database
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance = customer)

        if formset.is_valid():
            formset.save()

            # method to redirect to the dashboard page
            return redirect('/')

    context = {'formset': formset}

    # rendering the page
    return render(request, 'accounts/order_form.html', context)

# login in required to view these pages
# if not logged in then the user id redirected to the login page
@login_required(login_url='login') 
def updateOrder(request, pk):
    order = Order.objects.get(id = pk)
    # setting the instance of the form to the current order
    # 'instance' is for setting all options at once
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

# login in required to view these pages
# if not logged in then the user id redirected to the login page
@login_required(login_url='login') 
def deleteOrder(request, pk):
    order = Order.objects.get(id = pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {
        'item': order
    }

    return render(request, 'accounts/delete.html', context)