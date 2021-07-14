# Generated by Django 3.2.5 on 2021-07-15 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='user',
            field=models.OneToOneField(default='identity', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
