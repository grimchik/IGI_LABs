# Generated by Django 5.0.6 on 2024-05-27 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_order_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.company'),
        ),
    ]
