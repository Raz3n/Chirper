# Generated by Django 3.0.4 on 2020-06-07 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chirps', '0005_chirp_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chirp',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chirps', to=settings.AUTH_USER_MODEL),
        ),
    ]
