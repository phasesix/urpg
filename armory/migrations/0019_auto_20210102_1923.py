# Generated by Django 2.2.14 on 2021-01-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0018_riotgear_evasion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weaponmodificationattributechange',
            name='attribute',
            field=models.CharField(choices=[('attacks_per_action', 'attacksperaction'), ('capacity', 'capacity'), ('wounds', 'wounds'), ('penetration', 'penetration'), ('accuracy', 'accuracy'), ('weight', 'weight'), ('recoil_control', 'recoilcontrol'), ('concealment', 'concealment'), ('reload_actions', 'reloadactions')], max_length=40, verbose_name='attribute'),
        ),
    ]
