# Generated by Django 2.0.5 on 2018-10-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0012_auto_20181013_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='creation_mode',
            field=models.CharField(default='random', max_length=10, verbose_name='creation mode'),
        ),
    ]
