# Generated by Django 5.1.1 on 2024-09-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_market', '0006_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
