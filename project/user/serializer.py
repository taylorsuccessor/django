
from rest_framework import serializers
from models import MyUser as model








class Serializer(serializers.ModelSerializer):

    class Meta:
        model = model