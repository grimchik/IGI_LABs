# Generated by Django 5.0.6 on 2024-05-26 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_review_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='article',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main.article'),
        ),
    ]
