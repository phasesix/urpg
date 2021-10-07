# Generated by Django 2.0.13 on 2019-07-30 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0030_auto_20190730_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledge',
            name='extensions',
            field=models.ManyToManyField(to='rules.Extension'),
        ),
        migrations.AddField(
            model_name='lineage',
            name='extensions',
            field=models.ManyToManyField(to='rules.Extension'),
        ),
        migrations.AddField(
            model_name='shadow',
            name='extensions',
            field=models.ManyToManyField(to='rules.Extension'),
        ),
        migrations.AddField(
            model_name='skill',
            name='extensions',
            field=models.ManyToManyField(to='rules.Extension'),
        ),
        migrations.AddField(
            model_name='template',
            name='extensions',
            field=models.ManyToManyField(to='rules.Extension'),
        ),
        migrations.AlterField(
            model_name='knowledge',
            name='extension',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rules.Extension'),
        ),
        migrations.AlterField(
            model_name='lineage',
            name='extension',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rules.Extension'),
        ),
        migrations.AlterField(
            model_name='shadow',
            name='extension',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rules.Extension'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='extension',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rules.Extension'),
        ),
        migrations.AlterField(
            model_name='template',
            name='extension',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rules.Extension'),
        ),
    ]