# Generated by Django 3.2.4 on 2021-07-15 19:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_wishlist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 7, 15, 19, 53, 28, 481005, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
