"""django-admin module"""
from django.contrib import admin

@admin.register
class ContactAdmin(admin.ModelAdmin):
    """ admin """
    list_display = ('name', 'email')
