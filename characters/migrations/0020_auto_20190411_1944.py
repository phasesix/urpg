# Generated by Django 2.0.13 on 2019-04-11 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0019_characterweapon_condition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characterweapon',
            options={'ordering': ('weapon__id',)},
        ),
    ]
