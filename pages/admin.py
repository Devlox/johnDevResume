from django.contrib import admin

# Contact module registation to admin side
from .models import Contact

# Contacts admin customization
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name','email')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
