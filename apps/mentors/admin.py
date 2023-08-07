from django.contrib import admin
from . import models


@admin.register(models.Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'is_active', 'course', 'month', 'tel', 'language', 'time_create', 'time_update']
    list_filter = ['is_active', 'time_create', 'time_update']
    list_editable = ['is_active']


@admin.register(models.WorkTimes)
class WorkTimesAdmin(admin.ModelAdmin):
    list_display = ['daystart', 'dayend', 'weekends', 'weekends']
    list_filter = ['daystart', 'dayend', 'weekends', 'weekends']


@admin.register(models.FavoriteMentor)
class FavoriteMentorAdmin(admin.ModelAdmin):
    list_display = ['user', 'mentor']
    list_filter = ['user', 'mentor']


@admin.register(models.MentorReview)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['mentor', 'user', 'created_at']
    list_filter = ['mentor', 'user', 'created_at']
