from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer
from .models import Product

# Create your views here.
class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()

