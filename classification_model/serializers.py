from django.contrib.auth.models import Group, User
from .models import PredictMark
from rest_framework import serializers


class PredictMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictMark
        fields = ['time_study', 'num_course']


