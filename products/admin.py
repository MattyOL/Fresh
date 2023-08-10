from django.contrib import admin
from .models import Product, Category, Discount, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'value',
        'dcode',
        'expirey_date',
    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
    'product',
    'rating',
    'content', 
    'created_by', 
    'create_at',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Review, ReviewAdmin)
