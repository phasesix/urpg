# Generated by Django 2.0.5 on 2018-10-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0015_auto_20181013_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatemodifier',
            name='attribute',
            field=models.CharField(blank=True, choices=[('base_intelligence', 'intelligence'), ('base_max_health', 'max health'), ('base_bonus_dice', 'bonus dice'), ('base_destiny_dice', 'destiny dice'), ('base_rerolls', 'rerolls'), ('base_deftness', 'deftness'), ('base_strength', 'strength'), ('base_attractiveness', 'attractiveness'), ('base_endurance', 'endurance'), ('base_resistance', 'resistance'), ('base_quickness', 'quickness'), ('base_openness', 'openness'), ('base_conscientiousness', 'conscientiousness'), ('base_extraversion', 'extraversion'), ('base_agreeableness', 'agreeableness'), ('base_neuroticism', 'neuroticism')], max_length=40, null=True, verbose_name='attribute'),
        ),
    ]