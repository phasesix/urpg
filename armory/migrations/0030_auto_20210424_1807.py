# Generated by Django 2.2.18 on 2021-04-24 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0029_auto_20210424_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weaponmodificationattributechange',
            old_name='modifier',
            new_name='attribute_modifier',
        ),
    ]
