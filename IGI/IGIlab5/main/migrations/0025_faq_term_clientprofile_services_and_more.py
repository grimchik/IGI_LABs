# Generated by Django 5.0.6 on 2024-05-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_remove_order_cargo_type_alter_order_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, unique=True, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=200, unique=True, verbose_name='Термин')),
                ('definition', models.TextField(verbose_name='Определение')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='services',
            field=models.ManyToManyField(blank=True, related_name='services', to='main.service'),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.CharField(default='default', max_length=200, null=True),
        ),
    ]