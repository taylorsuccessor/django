
from rest_framework import serializers
from .models import Candidate









class Serializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields ='__all__'

        write_only_fields =['resume']