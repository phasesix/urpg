# Generated by Django 3.2.3 on 2021-05-31 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0052_merge_20210531_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
    ]
