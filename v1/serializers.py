from rest_framework import serializers
from v1.models import Weight, Exercise, Lift

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ['owner','weight_value','record_date']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['exercise_type','length','time','description','record_date','owner']

class LiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lift
        fields = ['lift_type', 'completed_reps', 'attempted_reps', 'weight', 'record_date', 'owner']
