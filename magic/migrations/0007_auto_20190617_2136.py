# Generated by Django 2.0.13 on 2019-06-17 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0006_auto_20190617_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spellflavour',
            name='spell_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magic.SpellType', verbose_name='Spell Type'),
        ),
    ]
