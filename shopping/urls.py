from django.urls import path
from .views import indexView, contactView, aboutView, productsView, singleProductsView

urlpatterns = [
    path('', indexView, name='home'),
    path('contact/', contactView, name='contact'),
    path('about/', aboutView, name='about'),
    path('products/', productsView, name='product'),
    path('single', singleProductsView, name='single'),
]