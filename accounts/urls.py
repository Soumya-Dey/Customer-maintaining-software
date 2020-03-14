from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), # for home page
    path('products/', views.products), # for products page
    path('customer/', views.customer), # for customer page
]