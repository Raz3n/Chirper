# Generated by Django 3.0.4 on 2020-05-18 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chirps', '0004_auto_20200516_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='chirp',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chirps.Chirp'),
        ),
    ]
