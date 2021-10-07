# Generated by Django 3.2.5 on 2021-07-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0004_auto_20191011_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='backdrop_copyright',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='image copyright'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='backdrop_copyright_url',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='image copyright url'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='image_copyright',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='image copyright'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='image_copyright_url',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='image copyright url'),
        ),
        migrations.AddField(
            model_name='handout',
            name='image_copyright',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='image copyright'),
        ),
        migrations.AddField(
            model_name='handout',
            name='image_copyright_url',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='image copyright url'),
        ),
    ]