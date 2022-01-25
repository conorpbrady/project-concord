from django.db import models
from django.utils import timezone

# Create your models here.

class Weight(models.Model):
    weight_value = models.DecimalField(decimal_places=2, max_digits=5, default = 0)
    record_date = models.DateTimeField(default = timezone.now)
    owner = models.ForeignKey('auth.User', related_name = 'weight', on_delete=models.CASCADE, null=True)

class Exercise(models.Model):
    exercise_type = models.CharField( max_length = 16)
    length = models.DecimalField(decimal_places=2, max_digits = 5, default = 0)
    time = models.DecimalField(decimal_places=2, max_digits = 5, default = 0)
    description = models.CharField(max_length = 255)

    record_date = models.DateTimeField(default = timezone.now)
    owner = models.ForeignKey('auth.User', related_name = 'exercise', on_delete=models.CASCADE, null=True)

class Lift(models.Model):
    lift_type = models.CharField(max_length = 32)
    completed_reps = models.IntegerField()
    attempted_reps = models.IntegerField()
    lift_weight = models.DecimalField(decimal_places=2, max_digits=5, default=0)

    record_date = models.DateTimeField(default = timezone.now)
    owner = models.ForeignKey('auth.User', related_name = 'lift', on_delete=models.CASCADE, null=True)
