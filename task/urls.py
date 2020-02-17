from django.urls import path, include
from task.views import HomeView, CategoryView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('allcategory/',CategoryView.as_view(),name='allcategory'),
]