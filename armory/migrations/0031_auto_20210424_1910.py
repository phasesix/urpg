# Generated by Django 2.2.18 on 2021-04-24 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0030_auto_20210424_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='bonus_dice',
            field=models.IntegerField(default=0, verbose_name='bonus dice'),
        ),
        migrations.AlterField(
            model_name='weaponmodificationattributechange',
            name='attribute',
            field=models.CharField(choices=[('capacity', 'Capacity'), ('wounds', 'Bonus wounds'), ('bonus_dice', 'Bonus dice'), ('penetration', 'Penetration'), ('concealment', 'Concealment'), ('reload_actions', 'Reload actions'), ('range_meter', 'Range (meter)')], max_length=40, verbose_name='attribute'),
        ),
        migrations.AlterField(
            model_name='weaponmodificationattributechange',
            name='attribute_modifier',
            field=models.IntegerField(default=0, verbose_name='attribute modifier'),
        ),
    ]
