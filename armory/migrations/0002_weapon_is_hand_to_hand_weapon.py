# Generated by Django 2.0.5 on 2018-10-06 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='is_hand_to_hand_weapon',
            field=models.BooleanField(default=False, verbose_name='is hand to hand weapon'),
        ),
    ]
