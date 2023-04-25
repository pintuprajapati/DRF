from rest_framework import serializers
from .models import Student

# Validators - For "name should start with 'r' otherwise raise an error"
# Custom function/class validation which can be used anywhere thorough the code.
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("Name should start with r")

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

        # Explicitely mention the condition for multiple field
        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {
        #     {'name': {'read_only': True}}
        #     {'roll': {'read_only': True}}
        # }
        
        # if you want all the fields from model or exclude some fields
        # fields = '__all__'
        # exclude = ['roll']

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
    
    # Field Level Validation - For Single Field Validation
    # We will use field validation on "roll" here
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full') # if roll >= 200, then raise an error and show the msg 'sear full'
        return value

    # Object Level Validation - For Multiple Fields Validation
    def validate(self, data):
        # Here "data" is python dict
        # We will use object level validation on "name"  and "city" here
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data
            