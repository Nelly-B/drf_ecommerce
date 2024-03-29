from django.shortcuts import render
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from  rest_framework import viewsets
from .models import Category, Brand, Product
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing category
    """
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many = True)
        return Response(serializer.data)
    

class BrandViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing brands
    """
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many = True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing category
    """
    queryset = Product.objects.all()
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many = True)
        return Response(serializer.data)