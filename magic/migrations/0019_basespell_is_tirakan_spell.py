# Generated by Django 3.2.6 on 2021-09-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0018_alter_spelltemplatemodifier_attribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='basespell',
            name='is_tirakan_spell',
            field=models.BooleanField(default=False, verbose_name='is tirakan spell'),
        ),
    ]
