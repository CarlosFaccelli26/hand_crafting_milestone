from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path(
        '<int:product_id>/',
        views.product_detail,
        name='product_detail'),
    path(
        'review/<int:product_id>/',
        views.review,
        name='review'),
    path(
        'delelte_review/<int:productreview_id>/',
        views.delete_review,
        name='delete_review'),
    path('add/', views.add_product, name='add_product'),
    path(
        'edit/<int:product_id>/',
        views.edit_product,
        name='edit_product'),
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'),
    path(
        'add_to_wishlist/<int:product_id>',
        views.add_to_wishlist,
        name='add_to_wishlist'),
    path(
        'wishlist/',
        views.wishlist,
        name='wishlist'),
    path('remove/<int:product_id>',
        views.remove_from_wishlist,
        name='remove_from_wishlist')
]
