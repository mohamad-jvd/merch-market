# Generated by Django 5.1.1 on 2024-09-26 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0005_alter_comment_suggest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_useful',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_social.isuseful'),
        ),
    ]
