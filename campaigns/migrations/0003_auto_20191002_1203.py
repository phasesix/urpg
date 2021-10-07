# Generated by Django 2.2.5 on 2019-10-02 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20191002_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='epoch',
            field=models.ForeignKey(limit_choices_to={'is_epoch': True}, on_delete=django.db.models.deletion.CASCADE, related_name='campaign_epoch_set', to='rules.Extension', verbose_name='Epoch'),
        ),
    ]