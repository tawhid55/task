from django.urls import path

from .views import ProductAPIView, ProductCategoryAPIView

urlpatterns = [
    path('', ProductCategoryAPIView.as_view()),
    path('products/',ProductAPIView.as_view()), 
]