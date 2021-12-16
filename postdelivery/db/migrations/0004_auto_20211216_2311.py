# Generated by Django 3.2.9 on 2021-12-16 23:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('db', '0003_auto_20211216_1852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adressrecipient',
            options={'verbose_name': 'Адрес получателя', 'verbose_name_plural': 'Адреса получателей'},
        ),
        migrations.AlterModelOptions(
            name='adresssender',
            options={'verbose_name': 'Адрес отправителя', 'verbose_name_plural': 'Адреса отправителей'},
        ),
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'Контракт', 'verbose_name_plural': 'Контракты'},
        ),
        migrations.AlterModelOptions(
            name='recipient',
            options={'verbose_name': 'Получатель', 'verbose_name_plural': 'Получатели'},
        ),
        migrations.AlterModelOptions(
            name='route',
            options={'verbose_name': 'Маршрут', 'verbose_name_plural': 'Маршруты'},
        ),
        migrations.AlterField(
            model_name='contract',
            name='closing_date',
            field=models.DateTimeField(verbose_name='Дата закрытия'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена контракта'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='count_loader',
            field=models.PositiveSmallIntegerField(verbose_name='Количество грузчиков'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='loaders',
            field=models.ManyToManyField(related_name='loader_contracts', to=settings.AUTH_USER_MODEL, verbose_name='Список грузчиков'),
        ),
    ]
