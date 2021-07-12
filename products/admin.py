from django.contrib import admin
from .models import Product, Category, ProductReview, WishList, WishListItem


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
        'date_added',
    )


class WishListItemAdmin(admin.ModelAdmin):
    list_display = (
        'wishlist',
        'product',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(WishList, WishlistAdmin)
admin.site.register(WishListItem, WishListItemAdmin)
