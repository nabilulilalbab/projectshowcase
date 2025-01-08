
from django.contrib import admin
from django.urls import path,include
from .views import index,about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("about/",about,name="about"),
    path("olshopthrift/",include("olshopthrift.urls",namespace="olshopthrift")),
    path("",index , name="index"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
