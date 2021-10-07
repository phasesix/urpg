# Generated by Django 3.2.5 on 2021-07-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0013_auto_20210726_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='spelltype',
            name='image_copyright',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='image copyright'),
        ),
        migrations.AddField(
            model_name='spelltype',
            name='image_copyright_url',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='image copyright url'),
        ),
        migrations.AlterField(
            model_name='spelltype',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='spelltype_images', verbose_name='image'),
        ),
    ]
