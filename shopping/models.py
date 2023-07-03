from django.db import models

# Create your models here.
class Cotegory(models.Model):
    name = models.TextField(max_length=122)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()
    
    def __str__(self) -> str:
        return self.name