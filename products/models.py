from django.db import models
from django.db.models import Avg, Count
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rate = models.ForeignKey(
        'ProductReview',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='products')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def rate_avarage(self):
        reviews_avarage = ProductReview.objects.filter(
            product=self).aggregate(
                avarage=Avg('rate'))
        avg = 0
        if reviews_avarage['avarage'] is not None:
            avg = float(reviews_avarage['avarage'])
        return avg
    
    def count_reviews(self):
        reviews_count = ProductReview.objects.filter(
            product=self).aggregate(
                count=Count('id'))
        count = 0
        if reviews_count['count'] is not None:
            count = int(reviews_count['count'])
        return count


RATE_CHOICES = [
    (1, 'Horrible'),
    (2, 'Bad'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent'),
]


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(
        'Product',
        related_name='reviews',
        on_delete=models.CASCADE,
        null=True)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(choices=RATE_CHOICES, blank=True, null=True)

    class Meta:
        ordering = ['-date', ]

    def __str__(self):
        return self.content


class Wishlist(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='wishlist')
    products = models.ManyToManyField(
        Product,
        through='WishlistItem')

    class Meta:
        verbose_name = 'Whis Lsit'
        verbose_name_plural = 'Wish Lists'
        
    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(
        Wishlist,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='wishlist_items')
    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='wishlist_products')
    added = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True)

    class Meta:
        verbose_name = 'Wish List Item'
        verbose_name_plural = 'Wish lists Items'
        ordering = ['-added', ]

    def __str__(self):
        return self.product.name
