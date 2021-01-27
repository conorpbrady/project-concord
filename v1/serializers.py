from rest_framework import serializers
from v1.models import Weight

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ['weight_value','record_date']
