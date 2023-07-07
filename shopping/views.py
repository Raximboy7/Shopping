from django.shortcuts import render


# Create your views here.


def indexView(request):
    ctx = {}
    return render(request, 'blog/index.html')


def contactView(request):
    ctx = {}
    return render(request, 'blog/contact.html')


def aboutView(request):
    ctx = {}
    return render(request, 'blog/about.html')



def productsView(request):
    ctx = {}
    return render(request, 'blog/products.html')


def singleProductsView(request):
    ctx = {}
    return render(request, 'blog/single-products.html')
