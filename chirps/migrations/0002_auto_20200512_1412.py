# Generated by Django 3.0.4 on 2020-05-12 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chirps', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chirp',
            options={'ordering': ['-id']},
        ),
    ]
