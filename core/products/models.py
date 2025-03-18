from django.db import models

# Category Model
class Category(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]

    page_title = models.CharField(max_length=255)
    meta_tag = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="subcategories")
    category_title = models.CharField(max_length=255)
    category_desc = models.TextField(blank=True, null=True)
    category_image = models.ImageField(upload_to='categories/images/', blank=True, null=True)
    category_image_name = models.CharField(max_length=255, blank=True, null=True)
    sort_order_number = models.IntegerField(default=0)
    active_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')

    def __str__(self):
        if self.parent_category:
            return f">> {self.parent_category} > {self.category_title}"
        return self.category_title

# Product Model
class Product(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]

    CHOICES = [
        ('link', 'Link'),
        ('document', 'Document')
    ]

    page_title = models.CharField(max_length=255)
    meta_tag = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    product_title = models.CharField(max_length=255)
    product_code = models.CharField(max_length=100)
    fluidlok_heading = models.CharField(max_length=255, blank=True, null=True)
    choose_either = models.CharField(max_length=10, choices=CHOICES, default='link')
    fluidlok_information = models.TextField(blank=True, null=True)
    fluidlok_image = models.ImageField(upload_to='products/fluidlok/', blank=True, null=True)
    fluidlok_image_name = models.CharField(max_length=255, blank=True, null=True)
    product_features = models.TextField(blank=True, null=True)
    product_specification = models.TextField(blank=True, null=True)
    product_image1 = models.ImageField(upload_to='products/images/', blank=True, null=True)
    product_image1_name = models.CharField(max_length=255, blank=True, null=True)
    product_image2 = models.ImageField(upload_to='products/images/', blank=True, null=True)
    product_image2_name = models.CharField(max_length=255, blank=True, null=True)
    product_large_image = models.ImageField(upload_to='products/large_images/', blank=True, null=True)
    sort_order_number = models.IntegerField(default=0)
    active_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')
    coming_soon = models.BooleanField(default=False)

    def __str__(self):
        return self.product_title
