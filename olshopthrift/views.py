from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    all_products = Product.objects.all()
    return render(request,"olshopthrift/index.html",context={
        "judul" : "thrift shop",
        "heading" : "page shop",
        "allproduct" : all_products,
    })

def detail_product(request,slugInput):
    detail_products = Product.objects.get(slug_prdt=slugInput)
    return render(request,"olshopthrift/detail.html",context={
        "judul" : "detail product",
        "heading" : "page detail",
        "detail" : detail_products,
    })

def kategori(request,kategoriInput):
    temp = Product.objects.filter(kategori__nama=kategoriInput)
    category = Product.objects.values("kategori__nama").distinct()
    return render(request,"olshopthrift/index.html",context={
        "judul" : " product",
        "heading" : "page ",
        "allproduct" : temp,
        "categories" : category,
    })