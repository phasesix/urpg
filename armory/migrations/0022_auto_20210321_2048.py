# Generated by Django 2.2.18 on 2021-03-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0021_auto_20210321_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weapon',
            name='attacks_per_action',
        ),
        migrations.AddField(
            model_name='weaponattackmode',
            name='dice_bonus',
            field=models.IntegerField(default=1, verbose_name='dice bonus'),
        ),
        migrations.AlterField(
            model_name='weaponmodificationattributechange',
            name='attribute',
            field=models.CharField(choices=[('capacity', 'capacity'), ('wounds', 'wounds'), ('penetration', 'penetration'), ('weight', 'weight'), ('recoil_control', 'recoilcontrol'), ('concealment', 'concealment'), ('reload_actions', 'reloadactions')], max_length=40, verbose_name='attribute'),
        ),
    ]
