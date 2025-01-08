
from django.contrib import admin
from .views import index,about
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    path("about/",about,name="about"),
    path("olshopthrift/",include("olshopthrift.urls",namespace="olshopthrift")),
    path("",index , name="index"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
