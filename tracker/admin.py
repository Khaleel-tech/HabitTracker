from django.contrib import admin

from .models import Habit, HabitLog


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


@admin.register(HabitLog)
class HabitLogAdmin(admin.ModelAdmin):
    list_display = ('habit', 'date', 'done', 'minutes')
    list_filter = ('date', 'done', 'habit')
