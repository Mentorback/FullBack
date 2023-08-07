from django.contrib import admin
from apps.others import models


@admin.register(models.Admin)
class Admin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'position']
    list_filter = ['first_name', 'last_name', 'position']


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'created_add']
    list_filter = ['user', 'text', 'created_add']
