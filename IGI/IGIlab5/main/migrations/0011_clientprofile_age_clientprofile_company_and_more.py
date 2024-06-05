# Generated by Django 5.0.6 on 2024-05-27 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_clientprofile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='age',
            field=models.PositiveIntegerField(default=18),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='company',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.company'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='vehicle',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.vehicle'),
        ),
    ]