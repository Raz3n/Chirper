# Generated by Django 3.0.4 on 2020-06-12 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200607_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followerrelation',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
    ]
