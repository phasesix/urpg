# Generated by Django 2.0.5 on 2018-10-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0015_auto_20181013_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='base_max_health',
            field=models.IntegerField(default=6, verbose_name='max health'),
        ),
        migrations.AddField(
            model_name='character',
            name='boost',
            field=models.IntegerField(default=0, verbose_name='boost'),
        ),
        migrations.AddField(
            model_name='character',
            name='health',
            field=models.IntegerField(default=6, verbose_name='health'),
        ),
    ]
