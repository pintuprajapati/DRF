from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Model Object - Single Student Data - // http://127.0.0.1:8000/api/stuinfo/2/
def student_detail(request, pk):
    stu = Student.objects.get(id=pk) # single data - Complex data

    serializer = StudentSerializer(stu) # converting model instance (complex data) into serialized data (Python Object)
    print("➡ serializer.data :", serializer.data) # output (assume id=2): {'id': 2, 'name': 'Raj', 'roll': 2, 'city': 'Agra'}

    json_data = JSONRenderer().render(serializer.data) # Rendering serialized data into JSON format. So that Front End can use it
    print("➡ json_data :", json_data) # output (assume id=2): b'{"id": 2, "name":"Raj","roll":2,"city":"Agra"}'

    return HttpResponse(json_data, content_type='application/json') # Sending JSON format data to Front End

    # By using JsonResponse(), we can get JSON format result in 1 line, insteaded of using 2 methods: JSONRenderer() and HttpResponse()
    # serializer.data is already "dict" type, so we don't have to set "safe=True"
    # return JsonResponse(serializer.data)


# Queryset Object - All Student Data - // http://127.0.0.1:8000/api/stuinfo/
def student_list(request):
    stu = Student.objects.all() # all data - Complex data

    # converting queryset instance (complex data) into serialized data (Python Object), We used "many=True" because here we are getting more than 1 object in queryset
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data) # Rendering serialized data into JSON format. So that Front End can use it
    return HttpResponse(json_data, content_type='application/json') # Sending JSON format data to Front End

    ## By using JsonResponse(), we can get JSON format result in 1 line, insteaded of using 2 methods: JSONRenderer() and HttpResponse()
    ## serializer.data is not "dict" type, so we have to set "safe=False"
    # return JsonResponse(serializer.data, safe=False)
