# Generated by Django 3.2.7 on 2021-10-04 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0033_auto_20210726_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riotgear',
            name='protection_explosive',
        ),
    ]
