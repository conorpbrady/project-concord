from django.db import models
from django.utils import timezone

# Create your models here.

class Weight(models.Model):
    weight_value = models.DecimalField(decimal_places=2, max_digits=5, default = 0)
    record_date = models.DateTimeField(default = timezone.now)
    owner = models.ForeignKey('auth.User', related_name = 'weight', on_delete=models.CASCADE, null=True)
