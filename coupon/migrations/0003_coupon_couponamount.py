# Generated by Django 3.0.5 on 2020-05-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0002_auto_20200428_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='couponAmount',
            field=models.IntegerField(default=50),
        ),
    ]
