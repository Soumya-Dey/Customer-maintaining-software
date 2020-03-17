from django.urls import path
from . import views

urlpatterns = [
    # for home page
    path('', views.home, name="home"),
    # for products page
    path('products/', views.products, name="products"),
    # for customer page [pk or primary key here is the customer id]
    path('customer/<str:pk>/', views.customer, name="customer"),
    # for create order page
    path('create_order/', views.createOrder, name="create_order"),
    # for update order page
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    # for delete order page
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]