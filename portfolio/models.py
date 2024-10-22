from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "Portfolio Category"

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to='images/portfolio')
    content = CKEditor5Field('Content', config_name='default', null=True)
    slug = models.SlugField(max_length=200, default="")
    category = models.ForeignKey('Category', related_name='category', on_delete=models.CASCADE)
    
    class Meta: 
        verbose_name_plural = "Portfolio"
    
    #Display Portfolio Title on Admin Panel
    def __str__(self):
        return self.title

class PortfolioImage(models.Model):
    post = models.ForeignKey('Portfolio', related_name='portfolioimages', on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/portfolio', null=True)
    images_alt_tag = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.post.title
        