# Generated by Django 3.1.5 on 2021-06-03 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('v1', '0004_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lift_type', models.CharField(max_length=32)),
                ('completed_reps', models.IntegerField()),
                ('attempted_reps', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('record_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lift', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]