# Generated by Django 5.1.1 on 2024-10-03 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0007_alter_comment_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='point',
        ),
        migrations.AddField(
            model_name='comment',
            name='negative_points',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='positive_points',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Point',
        ),
    ]
