# Generated by Django 2.0.13 on 2019-04-20 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0022_remove_character_reputation_spent'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='arcana',
            field=models.IntegerField(default=6, verbose_name='arcana'),
        ),
        migrations.AddField(
            model_name='character',
            name='base_max_arcana',
            field=models.IntegerField(default=3, verbose_name='max arcana'),
        ),
    ]
