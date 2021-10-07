# Generated by Django 2.0.5 on 2018-06-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0005_auto_20180507_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatemodifier',
            name='attribute',
            field=models.CharField(blank=True, choices=[('base_intelligence', 'Intelligenz'), ('base_bonus_dice', 'Bonuswürfel'), ('base_destiny_dice', 'Schicksalswürfel'), ('base_rerolls', 'Wiederholungswürfel'), ('base_deftness', 'Geschick'), ('base_strength', 'Kraft'), ('base_attractiveness', 'Attraktivität'), ('base_endurance', 'Ausdauer'), ('base_resistance', 'Resistenz'), ('base_quickness', 'Schnelligkeit'), ('base_openness', 'Offenheit'), ('base_conscientiousness', 'Gewissenhaftigkeit'), ('base_extraversion', 'Extraversion'), ('base_agreeableness', 'Verträglichkeit'), ('base_neuroticism', 'Neurotizismus')], max_length=40, null=True, verbose_name='Attribut'),
        ),
    ]