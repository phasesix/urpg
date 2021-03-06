# Generated by Django 2.0.13 on 2019-06-17 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0005_auto_20190617_1523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spellrule',
            options={'ordering': ('id',), 'verbose_name': 'spell rule', 'verbose_name_plural': 'spell rules'},
        ),
        migrations.AddField(
            model_name='spellflavour',
            name='spell_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='magic.SpellType'),
            preserve_default=False,
        ),
    ]
