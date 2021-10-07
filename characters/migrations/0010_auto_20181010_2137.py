# Generated by Django 2.0.5 on 2018-10-10 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_auto_20181010_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Charaktere ohne Benutzer werden täglich gelöscht.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Erzeugt von'),
        ),
        migrations.AlterField(
            model_name='characteritem',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Menge'),
        ),
        migrations.AlterField(
            model_name='characterriotgear',
            name='condition',
            field=models.IntegerField(default=100, verbose_name='Zustand'),
        ),
    ]
