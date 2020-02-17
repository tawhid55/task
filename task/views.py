from django.views.generic import TemplateView,ListView
from task.models import Product, Category

class HomeView(ListView):
    model = Product
    template_name = "home.html"

class CategoryView(ListView):
    model = Category
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['product_list'] = Product.objects.all()
        return context
    