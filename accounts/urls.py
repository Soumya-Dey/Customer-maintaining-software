from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), # for home page
    path('products/', views.products, name="products"), # for products page
    path('customer/<str:pk>/', views.customer, name="customer"), # for customer page
]