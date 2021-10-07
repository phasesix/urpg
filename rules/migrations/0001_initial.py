# Generated by Django 2.0.5 on 2018-05-04 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_mandatory', models.BooleanField(default=False, verbose_name='Ist Pflicht')),
                ('name_de', models.CharField(max_length=120, verbose_name='Name')),
                ('name_en', models.CharField(blank=True, max_length=120, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Erweiterung',
                'verbose_name_plural': 'Erweiterungen',
            },
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_de', models.CharField(max_length=120, verbose_name='Name')),
                ('name_en', models.CharField(blank=True, max_length=120, null=True, verbose_name='Name')),
                ('add_to_all_characters', models.BooleanField(default=True, verbose_name='Zu allen Charakteren hinzufügen')),
                ('extension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.Extension')),
            ],
            options={
                'verbose_name': 'Wissen',
                'verbose_name_plural': 'Wissen',
            },
        ),
        migrations.CreateModel(
            name='Shadow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_de', models.CharField(max_length=120, verbose_name='Name')),
                ('name_en', models.CharField(blank=True, max_length=120, null=True, verbose_name='Name')),
                ('extension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.Extension')),
            ],
            options={
                'verbose_name': 'Schatten',
                'verbose_name_plural': 'Schatten',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_de', models.CharField(max_length=120, verbose_name='Name')),
                ('name_en', models.CharField(blank=True, max_length=120, null=True, verbose_name='Name')),
                ('add_to_all_characters', models.BooleanField(default=True, verbose_name='Zu allen Charakteren hinzufügen')),
                ('extension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.Extension')),
            ],
            options={
                'verbose_name': 'Fertigkeit',
                'verbose_name_plural': 'Fertigkeiten',
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_de', models.CharField(max_length=120, verbose_name='Name')),
                ('name_en', models.CharField(blank=True, max_length=120, null=True, verbose_name='Name')),
                ('description_de', models.TextField(blank=True, null=True, verbose_name='Beschreibung')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Beschreibung')),
                ('cost', models.IntegerField(default=1, verbose_name='Kosten')),
            ],
            options={
                'verbose_name': 'Charaktervorlage',
                'verbose_name_plural': 'Charaktervorlagen',
            },
        ),
        migrations.CreateModel(
            name='TemplateCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_de', models.CharField(max_length=120, verbose_name='Name')),
                ('name_en', models.CharField(blank=True, max_length=120, null=True, verbose_name='Name')),
                ('description_de', models.TextField(blank=True, null=True, verbose_name='Beschreibung')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Vorlagenkategorie',
                'verbose_name_plural': 'template categories',
            },
        ),
        migrations.CreateModel(
            name='TemplateModifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(blank=True, choices=[('base_intelligence', 'Intelligenz'), ('base_deftness', 'Geschick'), ('base_strength', 'Kraft'), ('base_attractiveness', 'Attraktivität'), ('base_endurance', 'Ausdauer'), ('base_resistance', 'Resistenz'), ('base_quickness', 'Schnelligkeit'), ('base_openness', 'Offenheit'), ('base_conscientiousness', 'Gewissenhaftigkeit'), ('base_extraversion', 'Extraversion'), ('base_agreeableness', 'Verträglichkeit'), ('base_neuroticism', 'Neurotizismus')], help_text='Leer lassen wenn Wissens- oder Fertigkeitsmodifikatoren benutzt werden.', max_length=40, null=True, verbose_name='Attribut')),
                ('attribute_modifier', models.IntegerField(blank=True, help_text='Leer lassen wenn Wissens- oder Fertigkeitsmodifikatoren benutzt werden.', null=True, verbose_name='Attributsmodifikator')),
                ('skill_modifier', models.IntegerField(blank=True, help_text='Leer lassen wenn Attribut- oder Wissensmodifikatoren benutzt werden.', null=True, verbose_name='Fertigkeitsmodifikator')),
                ('knowledge_modifier', models.IntegerField(blank=True, help_text='Leer lassen wenn Fertigkeits- oder Attributsmodifikatoren benutzt werden.', null=True, verbose_name='Wissensmodifikator')),
                ('knowledge', models.ForeignKey(blank=True, help_text='Leer lassen wenn Fertigkeits- oder Attributsmodifikatoren benutzt werden.', null=True, on_delete=django.db.models.deletion.CASCADE, to='rules.Knowledge', verbose_name='Wissen')),
                ('skill', models.ForeignKey(blank=True, help_text='Leer lassen wenn Attribut- oder Wissensmodifikatoren benutzt werden.', null=True, on_delete=django.db.models.deletion.CASCADE, to='rules.Skill', verbose_name='Fertigkeit')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.Template', verbose_name='Vorlage')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='required_template_requirement_set', to='rules.Template')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.Template', verbose_name='Vorlage')),
            ],
        ),
        migrations.AddField(
            model_name='template',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.TemplateCategory', verbose_name='Kategorie'),
        ),
        migrations.AddField(
            model_name='template',
            name='extension',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.Extension'),
        ),
    ]
