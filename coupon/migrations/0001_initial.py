# Generated by Django 3.0.5 on 2020-04-24 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couponTitle', models.CharField(max_length=64)),
                ('couponCode', models.CharField(max_length=32, unique=True)),
                ('expirationDate', models.DateField(default=django.utils.timezone.now)),
                ('discountRate', models.IntegerField(default=0)),
                ('discountAmount', models.IntegerField(default=0)),
                ('couponDescription', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]
