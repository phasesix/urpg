# Generated by Django 2.2.14 on 2020-07-05 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0038_statuseffect'),
        ('characters', '0031_character_quirks'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterStatusEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_value', models.IntegerField(default=0, verbose_name='base value')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.Character')),
                ('status_effect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.StatusEffect')),
            ],
            options={
                'ordering': ('knowledge__name_en',),
            },
        ),
    ]
