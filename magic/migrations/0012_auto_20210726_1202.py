# Generated by Django 3.2.5 on 2021-07-26 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0011_auto_20210726_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpellShape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_de', models.CharField(max_length=30, verbose_name='name')),
                ('name_en', models.CharField(blank=True, max_length=30, null=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'spell shape',
                'verbose_name_plural': 'spell shapes',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='SpellTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_de', models.CharField(max_length=120, verbose_name='name')),
                ('name_en', models.CharField(blank=True, max_length=120, null=True, verbose_name='name')),
                ('cost', models.IntegerField(default=1, verbose_name='cost')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('rules_de', models.TextField(blank=True, null=True, verbose_name='rules')),
                ('rules_en', models.TextField(blank=True, null=True, verbose_name='rules')),
                ('quote', models.TextField(blank=True, null=True, verbose_name='quote')),
                ('quote_author', models.CharField(blank=True, max_length=50, null=True, verbose_name='quote author')),
            ],
            options={
                'verbose_name': 'spell template',
                'verbose_name_plural': 'spell templates',
            },
        ),
        migrations.AddField(
            model_name='basespell',
            name='actions',
            field=models.IntegerField(default=1, verbose_name='actions'),
        ),
        migrations.AddField(
            model_name='basespell',
            name='is_ritual',
            field=models.BooleanField(default=False, verbose_name='is ritual'),
        ),
        migrations.AddField(
            model_name='basespell',
            name='power',
            field=models.IntegerField(default=1, verbose_name='power'),
        ),
        migrations.AddField(
            model_name='basespell',
            name='range',
            field=models.IntegerField(default=0, verbose_name='range'),
        ),
        migrations.CreateModel(
            name='SpellTemplateModifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(blank=True, choices=[('power', 'power'), ('range', 'range'), ('actions', 'actions')], max_length=40, null=True, verbose_name='attribute')),
                ('attribute_modifier', models.IntegerField(blank=True, null=True, verbose_name='attribute modifier')),
                ('shape_change', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='magic.spellshape', verbose_name='shape change')),
                ('spell_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magic.spelltemplate')),
                ('type_change', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='magic.spelltype', verbose_name='type change')),
                ('variant_change', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='magic.spellvariant', verbose_name='variant change')),
            ],
        ),
        migrations.AddField(
            model_name='basespell',
            name='shape',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='magic.spellshape', verbose_name='shape'),
        ),
    ]