from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at', 'is_verified')
    list_filter = ('is_verified', 'created_at')
    search_fields = ('full_name', 'email', 'text')
    list_editable = ('is_verified',)
    ordering = ('-created_at',)
