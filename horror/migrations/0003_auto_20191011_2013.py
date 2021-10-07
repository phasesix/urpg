# Generated by Django 2.0.13 on 2019-10-11 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horror', '0002_quirk_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quirkmodifier',
            name='attribute',
            field=models.CharField(blank=True, choices=[('base_intelligence', 'intelligence'), ('base_max_health', 'max health'), ('base_max_arcana', 'max arcana'), ('base_spell_points', 'spell points'), ('base_bonus_dice', 'bonus dice'), ('base_destiny_dice', 'destiny dice'), ('base_rerolls', 'rerolls'), ('base_deftness', 'deftness'), ('base_strength', 'strength'), ('base_attractiveness', 'attractiveness'), ('base_endurance', 'endurance'), ('base_resistance', 'resistance'), ('base_quickness', 'quickness'), ('base_openness', 'openness'), ('base_conscientiousness', 'conscientiousness'), ('base_extraversion', 'extraversion'), ('base_agreeableness', 'agreeableness'), ('base_neuroticism', 'neuroticism'), ('base_max_stress', 'max stress')], max_length=40, null=True, verbose_name='attribute'),
        ),
    ]