# Generated by Django 2.0.13 on 2019-04-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0021_auto_20181210_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='is_epoch',
            field=models.BooleanField(default=True, verbose_name='is epoch'),
        ),
    ]