# Generated by Django 3.1.5 on 2021-06-02 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('v1', '0003_weight_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_type', models.CharField(max_length=16)),
                ('length', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('time', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('description', models.CharField(max_length=255)),
                ('record_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
