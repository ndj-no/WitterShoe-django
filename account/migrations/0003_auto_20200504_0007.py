# Generated by Django 3.0.5 on 2020-05-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='messengerId',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]