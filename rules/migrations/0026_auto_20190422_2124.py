# Generated by Django 2.0.13 on 2019-04-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0025_extension_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='identifier',
            field=models.CharField(max_length=20, verbose_name='identifier'),
        ),
    ]
