from rest_framework import serializers

from task.models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = ('__all__')

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = ('__all__')