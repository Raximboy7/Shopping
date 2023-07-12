from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cotegory(models.Model):
    name = models.TextField(max_length=122)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    cotegory = models.ForeignKey('Cotegory' , on_delete= models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    
      
    def __str__(self) -> str:
        return self.title
    
    
class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name='orders',
    )
    title = models.ForeignKey('Product',on_delete=models.CASCADE )
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    order_date = models.DateField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.name