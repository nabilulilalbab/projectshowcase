from django.db import models
from django.utils.text import slugify


# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    slug_kat = models.SlugField(editable=False,blank=True)

    def save(self,*args, **kwargs):
        self.slug_kat = slugify(self.nama)
        return super(Kategori,self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.id} {self.nama}"



class Product(models.Model):
    judul = models.CharField(max_length=255)
    description = models.TextField()
    kategori = models.ForeignKey(Kategori,on_delete=models.CASCADE)
    slug_prdt = models.SlugField(editable=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upddated_at = models.DateTimeField(auto_now=True)
    harga = models.IntegerField(default=0)
    images = models.ImageField(blank=True,default='default.png')
    is_hot = models.BooleanField(default=False)
    def save(self,*args, **kwargs):
        self.slug_prdt = slugify(self.judul)
        return super(Product,self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.id} {self.judul}"