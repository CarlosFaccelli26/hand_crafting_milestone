# Generated by Django 3.2.4 on 2021-07-12 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_wishlist_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
