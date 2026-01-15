from rest_framework import serializers
from .models import WorkoutPlan, WorkoutTask

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'

class WorkoutTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutTask
        fields = '__all__'
