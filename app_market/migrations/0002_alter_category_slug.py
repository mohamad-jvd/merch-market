# Generated by Django 5.1.1 on 2024-09-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
