from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()


class CategoryManager(models.Manager):
    def get_queryset(self):
        qs = super(CategoryManager, self).get_queryset()
        return qs.annotate(num_products=Count('product'))

class Category(models.Model):
    title = models.CharField(max_length=300)
    objects = CategoryManager()

    def __str__(self):
        return self.title
        

class  Product(models.Model):
    mainimage = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.FloatField()

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('name','slug')
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'


class Order(models.Model):
    orderitems  = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username