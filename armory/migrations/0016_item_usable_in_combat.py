# Generated by Django 2.2.14 on 2020-09-20 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0015_auto_20191124_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='usable_in_combat',
            field=models.BooleanField(default=False, verbose_name='usable in combat'),
        ),
    ]