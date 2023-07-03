from django.db import models

# Create your models here.
class Cotegory(models.Model):
    name = models.TextField(max_length=122)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    cotegory = models.ForeignKey('Cotegory' , on_delete= models.CASCADE, related_name='product')
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    
class Order(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
        related_name='orders',
    )
    title = models.ForeignKey('Product', related_name='order')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    order_date = models.DateField(auto_now_add=True)