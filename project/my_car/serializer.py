
from rest_framework import serializers
from models import MyCar

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCar