from rest_framework import serializers
from .models import F1Driver


class F1DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = F1Driver
        fields = ['id', 'driver_name', 'team',
                  'car_number', 'championship_points']
