# Generated by Django 5.1.1 on 2024-10-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0014_remove_comment_rate_alter_comment_negative_points_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rate',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='negative_points',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='positive_points',
            field=models.TextField(blank=True, null=True),
        ),
    ]