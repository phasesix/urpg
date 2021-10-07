# Generated by Django 2.2.14 on 2021-01-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0044_auto_20201222_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='default_persona_attribute',
            field=models.CharField(choices=[('intelligence', 'intelligence'), ('openness', 'openness'), ('conscientiousness', 'conscientiousness'), ('extraversion', 'extraversion'), ('agreeableness', 'agreeableness'), ('neuroticism', 'neuroticism')], default='openness', max_length=20, verbose_name='default persona attribute'),
        ),
    ]