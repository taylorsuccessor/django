
from rest_framework import serializers
from models import MyCar





class ClassNameField(serializers.Field):
    def get_attribute(self, obj):
        # We pass the object instance onto `to_representation`,
        # not just the field attribute.
        return obj

    def to_representation(self, obj):
        """
        Serialize the object's class name.
        """
        return 'to_representation'

    def to_internal_value(self, data):
        return {}







class CarSerializer(serializers.ModelSerializer):
    custom_field = serializers.SerializerMethodField('custom_field_method')
    name = serializers.SerializerMethodField('name_method')


    custom_field_class = ClassNameField(source='*')




    def name_method(self,obj):
        return 'override field'
    def custom_field_method(self, obj):
        return 'iiiiiiiiiiiii'+obj.name

    class Meta:
        model = MyCar