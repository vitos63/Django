from django.contrib.sitemaps import Sitemap
from .models import Women


class WomenSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Women.objects.all()
    
    def lastmod(self,obj):
        return obj.time_update