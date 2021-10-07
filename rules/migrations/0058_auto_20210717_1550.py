# Generated by Django 3.2.5 on 2021-07-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0057_skillchanges'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineage',
            name='base_intelligence',
        ),
        migrations.AlterField(
            model_name='templatemodifier',
            name='attribute',
            field=models.CharField(blank=True, choices=[('base_max_health', 'max health'), ('base_max_arcana', 'max arcana'), ('base_spell_points', 'spell points'), ('base_actions', 'actions'), ('base_bonus_dice', 'bonus dice'), ('base_destiny_dice', 'destiny dice'), ('base_rerolls', 'rerolls'), ('base_deftness', 'deftness'), ('base_strength', 'strength'), ('base_attractiveness', 'attractiveness'), ('base_endurance', 'endurance'), ('base_resistance', 'resistance'), ('base_quickness', 'quickness'), ('base_education', 'education'), ('base_logic', 'logic'), ('base_conscientiousness', 'conscientiousness'), ('base_willpower', 'willpower'), ('base_apprehension', 'apprehension'), ('base_charm', 'charm'), ('base_max_stress', 'max stress')], max_length=40, null=True, verbose_name='attribute'),
        ),
    ]
