# Generated by Django 2.0.13 on 2019-07-30 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0028_template_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='quote_author',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='quote author'),
        ),
    ]
