# Generated by Django 2.0.5 on 2018-09-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0007_auto_20180926_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='kind',
            field=models.CharField(choices=[('p', 'praktisch'), ('m', 'geistig')], max_length=1, verbose_name='kind'),
        ),
    ]
