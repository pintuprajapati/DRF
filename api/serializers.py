from rest_framework import serializers
from .models import Student

# Serializer using "ModelSerializer"
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only = True) # Explicitly mention the condition for specific single field
    class Meta:
        model = Student # create a ModelSerializer for "Student" model
        fields = ['id', 'name', 'roll', 'city']

        read_only_fields = ['name', 'roll'] # Explicitely mention the condition for multiple field

        # extra_kwargs = {
        #     'name': {'read_only': True},
        # }
    
        # if you want all the fields from model or exclude some fields
        # fields = '__all__'
        # exclude = ['roll']