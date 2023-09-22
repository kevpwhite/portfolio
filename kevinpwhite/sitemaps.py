from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from portfolio.models import Portfolio
from blog.models import Post

class PostSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def location(self, obj):
        return '/blog/%s' %(obj.slug)

class PortfolioSiteMap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Portfolio.objects.all()

    def location(self, obj):
        return '/portfolio/%s' %(obj.slug)

class StaticSitemap(Sitemap):
    changefreq= "yearly"
    priority = 1
    protocol = 'https'

    def items(self):
        return [
            'home:home',
            'portfolio:portfolio',
            'blog:blog',
        ]

    def location(self, item):
        return reverse(item)
        