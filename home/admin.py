from django.contrib import admin
from .models import ContactUs

# Admin display
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

# Register your models here for admin page
admin.site.register(ContactUs, ContactUsAdmin)
