# Generated by Django 2.0.13 on 2019-08-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0034_auto_20190811_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='extension_images', verbose_name='image'),
        ),
    ]
