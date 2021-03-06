# Generated by Django 3.2.5 on 2021-07-24 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0040_delete_characterspell'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magic', '0007_auto_20190617_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseSpell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_de', models.CharField(max_length=80, verbose_name='name')),
                ('name_en', models.CharField(blank=True, max_length=80, null=True, verbose_name='name')),
                ('rules_de', models.TextField(verbose_name='rules')),
                ('rules_en', models.TextField(blank=True, null=True, verbose_name='rules')),
                ('quote', models.TextField(blank=True, null=True, verbose_name='quote')),
                ('quote_author', models.CharField(blank=True, max_length=50, null=True, verbose_name='quote author')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magic.spelltype', verbose_name='type')),
            ],
            options={
                'verbose_name': 'base spell',
                'verbose_name_plural': 'base spell',
                'ordering': ('id',),
            },
        ),
        migrations.RemoveField(
            model_name='spellflavour',
            name='spell_type',
        ),
        migrations.AlterUniqueTogether(
            name='spellrule',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='spellrule',
            name='flavour',
        ),
        migrations.RemoveField(
            model_name='spellrule',
            name='power',
        ),
        migrations.DeleteModel(
            name='Spell',
        ),
        migrations.DeleteModel(
            name='SpellAreaOfEffect',
        ),
        migrations.DeleteModel(
            name='SpellAreaOfEffectRange',
        ),
        migrations.DeleteModel(
            name='SpellCastingTime',
        ),
        migrations.DeleteModel(
            name='SpellComponents',
        ),
        migrations.DeleteModel(
            name='SpellCost',
        ),
        migrations.DeleteModel(
            name='SpellFlavour',
        ),
        migrations.DeleteModel(
            name='SpellPower',
        ),
        migrations.DeleteModel(
            name='SpellRange',
        ),
        migrations.DeleteModel(
            name='SpellRule',
        ),
    ]
