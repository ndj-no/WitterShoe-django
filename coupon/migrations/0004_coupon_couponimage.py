# Generated by Django 3.0.5 on 2020-05-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0003_coupon_couponamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='couponImage',
            field=models.ImageField(blank=True, upload_to='coupon_images'),
        ),
    ]
