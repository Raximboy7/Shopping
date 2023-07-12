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
    ctg = Cotegory.objects.all()
    ctx = {
        'ctg':ctg
    }
    return render(request, 'blog/contact.html',ctx)


def aboutView(request):
    ctg = Cotegory.objects.all()
    ctx = {
        'ctg':ctg
    }
    return render(request, 'blog/about.html',ctx)



def productsView(request):
    ctg = Cotegory.objects.all()
    prd = Product.objects.all()
    ctx = {
        'ctg':ctg,
        'prd':prd
    }
    return render(request, 'blog/products.html',ctx)


def singleProductsView(request):
    ctg = Cotegory.objects.all()
    ctx = {
        'ctg':ctg
    }
    return render(request, 'blog/single-product.html')
