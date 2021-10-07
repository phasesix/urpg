# Generated by Django 2.0.5 on 2018-09-30 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0009_auto_20180930_1337'),
        ('characters', '0005_auto_20180630_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='lineage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rules.Lineage', verbose_name='lineage'),
        ),
    ]
