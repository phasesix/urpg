# Generated by Django 2.0.5 on 2018-05-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0004_auto_20180507_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatemodifier',
            name='attribute',
            field=models.CharField(blank=True, choices=[('base_intelligence', 'Intelligenz'), ('base_bonus_dice', 'bonus dice'), ('base_destiny_dice', 'destiny dice'), ('base_rerolls', 'rerolls'), ('base_deftness', 'Geschick'), ('base_strength', 'Kraft'), ('base_attractiveness', 'Attraktivität'), ('base_endurance', 'Ausdauer'), ('base_resistance', 'Resistenz'), ('base_quickness', 'Schnelligkeit'), ('base_openness', 'Offenheit'), ('base_conscientiousness', 'Gewissenhaftigkeit'), ('base_extraversion', 'Extraversion'), ('base_agreeableness', 'Verträglichkeit'), ('base_neuroticism', 'Neurotizismus')], max_length=40, null=True, verbose_name='Attribut'),
        ),
    ]
