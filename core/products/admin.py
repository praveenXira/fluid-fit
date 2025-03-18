from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'category_title',
        'parent_category',
        'active_status',
    )
    list_filter = ('active_status',)
    search_fields = ('category_title', 'meta_tag', 'meta_description')
    ordering = ('sort_order_number',)
    
    def formatted_category_title(self, obj):
        """Display categories in a hierarchical manner"""
        indent = ">> " if obj.parent_category else ""
        return f"{indent}{obj.category_title}"
    
    formatted_category_title.admin_order_field = 'category_title'
    formatted_category_title.short_description = "Category Title"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Customize the foreign key dropdown to show hierarchical category names"""
        if db_field.name == "parent_category":
            kwargs["queryset"] = Category.objects.all().order_by('sort_order_number')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product_category',  'product_title',
        'active_status'
    )
    list_filter = ('active_status', 'coming_soon', 'product_category')
    search_fields = ('product_title', 'product_code', 'meta_tag', 'meta_description')
    ordering = ('sort_order_number',)
