from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io

#Student Data - // http://127.0.0.1:8000/api/studentapi/
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body # Getting JSON data from Client
        stream = io.BytesIO(json_data) # converting JSON data to Stream
        python_data = JSONParser().parse(stream) # Parsing stream data to JSONParser() to convert stream into python data
        id = python_data.get('id', None) # Get 'id' from the python_data

        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu) # converting pythond data to complex data
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type = 'application/json')
            except Student.DoesNotExist:
                error_msg = 'Id does not exist'
                raise Exception(error_msg)
        else:
            # else return whole student object - return all the data
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')
    
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors) # if not validated. This will be returned
        return HttpResponse(json_data, content_type='application/json')
        
    if request.method == "PUT":
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=python_data, partial=True) # updating partially only. Updating some data, not all
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data Created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors) # if not validated. This will be returned
            return HttpResponse(json_data, content_type='application/json')
        except Student.DoesNotExist:
            error_msg = 'Id does not exist'
            raise Exception(error_msg)        
        
    if request.method == "DELETE":
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {'msg': 'Data Deleted!'}
            # json_data = JSONRenderer().render(res) # if not validated. This will be returned
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res, safe=False) # instead of 2 above 2 lines, we can just use JsonResponse() - One Liner
        except Student.DoesNotExist:
            error_msg = 'Id does not exist'
            raise Exception(error_msg)
        