# Generated by Django 2.2.14 on 2020-12-22 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0043_auto_20200921_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='description_de',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='extension',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='extension',
            name='year_range_de',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='year range'),
        ),
        migrations.AddField(
            model_name='extension',
            name='year_range_en',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='year range'),
        ),
    ]
