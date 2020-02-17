from rest_framework import generics

from task.models import Category, Product
from .serializers import ProductSerializer, ProductCategorySerializer

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductCategorySerializer
