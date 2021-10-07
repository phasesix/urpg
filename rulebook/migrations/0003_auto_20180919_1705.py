# Generated by Django 2.0.5 on 2018-09-19 17:05

from django.db import migrations, models
import simplemde.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rulebook', '0002_auto_20180630_1724'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ('number',), 'verbose_name': 'Kapitel', 'verbose_name_plural': 'Kapitel'},
        ),
        migrations.AddField(
            model_name='chapter',
            name='fa_icon_class',
            field=models.CharField(default='book', max_length=30, verbose_name='FA Icon Class'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.IntegerField(verbose_name='Nummer'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='text_de',
            field=simplemde.fields.SimpleMDEField(blank=True, null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='text_en',
            field=simplemde.fields.SimpleMDEField(blank=True, null=True, verbose_name='Text'),
        ),
    ]
