# Generated by Django 2.0.5 on 2018-09-26 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0006_auto_20180630_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='template',
            options={'ordering': ('category__id',), 'verbose_name': 'Charakterschablone', 'verbose_name_plural': 'Charakterschablonen'},
        ),
        migrations.RemoveField(
            model_name='skill',
            name='add_to_all_characters',
        ),
        migrations.AddField(
            model_name='skill',
            name='kind',
            field=models.CharField(choices=[('p', 'practical'), ('m', 'mind')], default='p', max_length=1, verbose_name='kind'),
            preserve_default=False,
        ),
    ]
