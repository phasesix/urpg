# Generated by Django 2.0.13 on 2019-04-28 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0003_auto_20190428_2043'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='spellrule',
            unique_together={('flavour', 'power')},
        ),
    ]