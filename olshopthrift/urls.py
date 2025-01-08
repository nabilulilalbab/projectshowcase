from django.urls import path
from .views import index,detail_product,kategori
app_name="olshopthrift"
urlpatterns = [
    path("",index,name="index"),
    path("detail/<slug:slugInput>/",detail_product,name="detail"),
    path("kategori/<slug:kategoriInput>/",kategori,name="kategori")
]
