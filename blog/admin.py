from django.contrib import admin
from .models import Post, PostCategory, PostImage
from mptt.admin import MPTTModelAdmin

class PostImageAdmin(admin.StackedInline):
    model = PostImage
    extra = 1

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines=  [PostImageAdmin]
    list_display = ('title', 'slug', 'status','created_on', 'updated_on')
    list_filter = ('status','category',)
    search_fields = ['title', 'content',]

class PostCategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {'slug': ('category',)}
    list_display = ('category', 'slug')
    list_filter = ('category',)
    search_fields = ['category', 'slug']


admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
# admin.site.register(PostCategory, MPTTModelAdmin)