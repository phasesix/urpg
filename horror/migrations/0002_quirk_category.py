# Generated by Django 2.0.13 on 2019-10-11 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horror', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quirk',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='horror.QuirkCategory', verbose_name='category'),
            preserve_default=False,
        ),
    ]