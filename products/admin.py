from django.contrib import admin
from .models import Product, Category, ProductReview, Wishlist, WishlistItem


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'rate',
        'image',
    )

    ordering = ['sku', ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'date',
        'rate',
        'user',
    )


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )


class WishlistItemAdmin(admin.ModelAdmin):
    list_display = (
        'wishlist',
        'product',
        'added',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(WishlistItem, WishlistItemAdmin)
