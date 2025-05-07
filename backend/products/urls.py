from django.urls import path
from . import views  # Import your views from the current directory

urlpatterns = [
    path('', views.ProductList.as_view(), name='product-list'),          # List and create products
    path('<int:pk>/', views.ProductDetail.as_view(), name='product-detail'), # Retrieve, update, delete a product
]