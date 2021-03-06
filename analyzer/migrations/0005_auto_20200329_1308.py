# Generated by Django 3.0.4 on 2020-03-29 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0004_auto_20200328_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseasestats',
            name='country',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='analyzer.Country'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='diseasestats',
            unique_together={('disease_season', 'country', 'stats_date')},
        ),
    ]
