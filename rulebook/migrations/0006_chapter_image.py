# Generated by Django 2.0.13 on 2019-08-25 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rulebook', '0005_auto_20180926_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='image',
            field=models.ImageField(blank=True, max_length=80, null=True, upload_to='chapter_images/', verbose_name='Bild'),
        ),
    ]
