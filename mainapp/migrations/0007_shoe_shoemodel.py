# Generated by Django 3.0.5 on 2020-05-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20200501_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='shoeModel',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]