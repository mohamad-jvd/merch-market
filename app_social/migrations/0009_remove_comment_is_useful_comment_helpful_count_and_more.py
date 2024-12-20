# Generated by Django 5.1.1 on 2024-10-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0008_remove_comment_point_comment_negative_points_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_useful',
        ),
        migrations.AddField(
            model_name='comment',
            name='helpful_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='not_helpful_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='IsUseful',
        ),
    ]
