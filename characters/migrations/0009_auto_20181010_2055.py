# Generated by Django 2.0.5 on 2018-10-10 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0008_characteritem_characterriotgear_characterweapon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Characters without user will be cleaned daily.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Erzeugt von'),
        ),
    ]
