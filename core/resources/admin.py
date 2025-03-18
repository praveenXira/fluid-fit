from django.contrib import admin
from .models import Industry, Certification, CertificationCategory, Download, DownloadCategory, Distributor

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name', 'coming_soon', 'active_status')
    list_editable = ('coming_soon', 'active_status')

@admin.register(CertificationCategory)
class CertificationCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'coming_soon', 'downloader_info')
    list_editable = ('coming_soon', 'downloader_info')

@admin.register(DownloadCategory)
class DownloadCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'coming_soon', 'downloader_info')
    list_editable = ('coming_soon', 'downloader_info')

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'country', 'state', 'city', 'email')
