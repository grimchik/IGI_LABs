# Generated by Django 5.0.6 on 2024-05-27 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_order_coupon_alter_service_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cargo_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.cargotype'),
        ),
    ]