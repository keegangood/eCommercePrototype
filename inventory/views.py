from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return Response({'products': products, 'categories':categories})

