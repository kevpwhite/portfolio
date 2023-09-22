from django.contrib import admin
from .models import Category, Portfolio, PortfolioImage

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
    search_fields =('title', 'category')
    prepopulated_fields = {'slug': ('title',)}

class PortfolioImageAdmin(admin.StackedInline):
    model = PortfolioImage

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageAdmin]
 
    class Meta:
       model = Portfolio
    
admin.site.register(Category)