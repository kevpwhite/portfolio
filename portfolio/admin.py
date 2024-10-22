from django.contrib import admin
from .models import Category, Portfolio, PortfolioImage

class PortfolioImageAdmin(admin.StackedInline):
    model = PortfolioImage
    extra = 1

class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PortfolioImageAdmin]
    list_display = ('title', 'slug', 'category',) 
    search_fields = ('title', 'category',)

admin.site.register(Category)
admin.site.register(Portfolio, PortfolioAdmin)
