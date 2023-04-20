from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io

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

## Deserialization - Converting Client's JSON data into Native Python Datatypes
@csrf_exempt
def student_create(request):
    """
    The purpose of using a 'stream' here is to convert the raw JSON data into a format that can be parsed by the JSONParser function. The JSONParser function expects the input data to be in stream format, which is why the JSON data is first converted into a stream before it is parsed.
    """
    if request.method == 'POST':
        json_data = request.body # Getting JSON data from Client
        stream = io.BytesIO(json_data) # converting JSON data to Stream
        python_data = JSONParser().parse(stream) # Parsing stream data to JSONParser() to convert stream into python data
        serializer = StudentSerializer(data=python_data) # converting pythond data to complex data
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors) # if not validated. This will be returned
        return HttpResponse(json_data, content_type='application/json')
