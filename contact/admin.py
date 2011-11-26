from contact.models import Contact
from django.contrib import admin

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'message', 'status')
admin.site.register(Contact, ContactAdmin)