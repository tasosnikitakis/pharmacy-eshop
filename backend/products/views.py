from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView): # For listing and creating
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView): # For retrieving, updating, and deleting a single product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer