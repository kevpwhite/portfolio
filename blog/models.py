from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
from mptt.models import MPTTModel, TreeForeignKey

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Post(models.Model):
    category = TreeForeignKey('PostCategory', null=True, on_delete=models.CASCADE, related_name='postcategory')
    title = models.CharField(max_length=200, unique=True)
    featured_image = models.ImageField(upload_to='images/blog', null=True)
    featured_img_alt_tag = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated_on = models.DateField(auto_now= True)
    content = CKEditor5Field('Content', config_name='default', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name_plural = "Post"
        ordering = ('-created_on',)

    def __str__(self):
        return self.title


class PostCategory(MPTTModel):
    category = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'Post Categories'

    def __str__(self):
        return self.category

class PostImage(models.Model):
    post = models.ForeignKey('Post', related_name='postimages', on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/blog', null=True)
    images_alt_tag = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.post.title    