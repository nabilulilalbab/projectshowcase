from django.shortcuts import render
from olshopthrift.models import Product

def index(request):
    latest_products = Product.objects.order_by('-created_at')[:4]
    return render(request,"index.html",context={
        "judul" : "home",
        "heading" : "landing page",
        'latest_products': latest_products,
    })

def about(request):
    return render(request,"about.html",context={})