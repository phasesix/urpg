# Generated by Django 3.2.5 on 2021-08-06 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0014_auto_20210726_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='spelltype',
            name='dominant_attribute',
            field=models.CharField(blank=True, choices=[('deftness', 'deftness'), ('strength', 'strength'), ('attractiveness', 'attractiveness'), ('endurance', 'endurance'), ('resistance', 'resistance'), ('quickness', 'quickness'), ('logic', 'logic'), ('education', 'education'), ('conscientiousness', 'conscientiousness'), ('willpower', 'willpower'), ('apprehension', 'apprehension'), ('charm', 'charm')], max_length=20, null=True, verbose_name='dominant attribute'),
        ),
    ]
