# Generated by Django 5.1.1 on 2024-09-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0003_rename_description_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
