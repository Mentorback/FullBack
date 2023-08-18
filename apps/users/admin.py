from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'course', 'month', 'is_mentor', 'created_at', 'updated_at']
    list_filter = ['is_mentor', 'created_at', 'updated_at']
    list_editable = ['is_mentor']
    list_display_links = ("name",)
    search_fields = ("name",)
    ordering = ("-created_at",)
