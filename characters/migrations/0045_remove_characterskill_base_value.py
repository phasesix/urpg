# Generated by Django 3.2.7 on 2021-10-04 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0044_auto_20211004_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterskill',
            name='base_value',
        ),
    ]
