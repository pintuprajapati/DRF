from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # to create data using POST
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # to update the data
    def update(self, instance, validated_data):
        """
        Params: 
            validation_data - New data from user for updation
            instance - Old data stored in database
        Return:
            It will return the instance with "updated value or old value"

        Ex: If the new data is available for 'name' then it will be 'get()' and updated in database.
        If new data for 'name' is not available then old instance of 'name' will remain the same. It won't change.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full') # if roll >= 200, then raise an error and show the msg 'sear full'
        return value