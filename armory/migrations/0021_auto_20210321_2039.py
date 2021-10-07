# Generated by Django 2.2.18 on 2021-03-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0020_auto_20210130_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weapon',
            name='accuracy',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='recoil_control',
        ),
        migrations.AlterField(
            model_name='weaponmodificationattributechange',
            name='attribute',
            field=models.CharField(choices=[('attacks_per_action', 'attacksperaction'), ('capacity', 'capacity'), ('wounds', 'wounds'), ('penetration', 'penetration'), ('weight', 'weight'), ('recoil_control', 'recoilcontrol'), ('concealment', 'concealment'), ('reload_actions', 'reloadactions')], max_length=40, verbose_name='attribute'),
        ),
    ]
