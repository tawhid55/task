from django.contrib import admin
from task.models import Category, Product, Order, Cart

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)

