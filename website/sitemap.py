from django.contrib import sitemaps
from django.urls import reverse

class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'locations', 'services', 'east-colfax-avenue',]

    def location(self, item):
        return reverse(item)   

