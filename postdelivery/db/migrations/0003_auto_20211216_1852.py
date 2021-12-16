# Generated by Django 3.2.9 on 2021-12-16 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('db', '0002_auto_20211210_0527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loaderslist',
            name='contract',
        ),
        migrations.RemoveField(
            model_name='loaderslist',
            name='loader',
        ),
        migrations.AddField(
            model_name='contract',
            name='loaders',
            field=models.ManyToManyField(related_name='loader_contracts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='client_contracts', to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='drive_contracts', to=settings.AUTH_USER_MODEL, verbose_name='Водитель'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='manager_contracts', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='Loader',
        ),
        migrations.DeleteModel(
            name='LoadersList',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]