from django.shortcuts import render
from .models import *

# Create your views here.

def indexView(request):
    ctg = Cotegory.objects.all()
    ctx = {
        'ctg':ctg
    }
    return render(request, 'blog/index.html',ctx)


def contactView(request):
    ctx = {}
    return render(request, 'blog/contact.html')


def aboutView(request):
    ctx = {}
    return render(request, 'blog/about.html')



def productsView(request):
    ctg = Cotegory.objects.all()
    prd = Product.objects.all()
    ctx = {
        'ctg':ctg,
        'prd':prd
    }
    return render(request, 'blog/products.html',ctx)


def singleProductsView(request):
    ctx = {}
    return render(request, 'blog/single-product.html')
