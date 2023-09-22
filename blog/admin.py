from django.contrib import admin
from .models import Post, PostCategory, PostImage
from mptt.admin import MPTTModelAdmin

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', 'video_url')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ("name",)
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Post

admin.site.register(PostCategory, MPTTModelAdmin)