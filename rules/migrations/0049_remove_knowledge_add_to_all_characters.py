# Generated by Django 2.2.18 on 2021-03-13 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0048_knowledge_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='knowledge',
            name='add_to_all_characters',
        ),
    ]
