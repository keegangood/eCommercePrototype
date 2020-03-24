from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

