# Generated by Django 3.2.7 on 2021-10-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0020_auto_20210930_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='spelltype',
            name='supplemental_attribute',
            field=models.CharField(blank=True, choices=[('deftness', 'deftness'), ('strength', 'strength'), ('attractiveness', 'attractiveness'), ('endurance', 'endurance'), ('resistance', 'resistance'), ('quickness', 'quickness'), ('logic', 'logic'), ('education', 'education'), ('conscientiousness', 'conscientiousness'), ('willpower', 'willpower'), ('apprehension', 'apprehension'), ('charm', 'charm')], max_length=20, null=True, verbose_name='supplemental attribute'),
        ),
    ]
