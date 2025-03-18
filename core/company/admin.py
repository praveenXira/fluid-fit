from django.contrib import admin
from .models import History, Approach, Career, Client, Testimonial, Document

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('year', 'heading', 'short_description')

@admin.register(Approach)
class ApproachAdmin(admin.ModelAdmin):
    list_display = ('heading', 'status', 'sequence')
    list_editable = ('status', 'sequence')

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('post', 'code', 'short_description')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_name', 'active_status')
    list_editable = ('active_status',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'designation', 'active_status')
    list_editable = ('active_status',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'active_status')
    list_editable = ('active_status',)
