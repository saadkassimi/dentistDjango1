from django.contrib import admin
from django.urls import path, include
from templates.sitemap import StaticViewsSitemap
from django.contrib import sitemaps
from website import models as website
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.views.generic.base import TemplateView #import TemplateView


sitemaps = {
    'sitemap': StaticViewsSitemap, 
        
    }

    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')

    
    ]

