from django.contrib import admin
from .models import News, NewsCategory, Event

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'exhibition_name', 'booth_number', 'venue')
