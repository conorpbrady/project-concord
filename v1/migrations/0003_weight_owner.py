# Generated by Django 3.1.5 on 2021-01-27 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('v1', '0002_auto_20210126_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='weight',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weight', to=settings.AUTH_USER_MODEL),
        ),
    ]
