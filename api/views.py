from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io

# In class based view - There is a different way to use csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

#Student Data - // http://127.0.0.1:8000/api/studentapi/
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    """
        GET, POST, PUT, DELETE methods defined
        Will return JSON response to the other end
    """
    # get data
    def get(self, request, *args, **kwargs):
        json_data = request.body # Getting JSON data from Client
        stream = io.BytesIO(json_data) # converting JSON data to Stream
        python_data = JSONParser().parse(stream) # Parsing stream data to JSONParser() to convert stream into python data
        id = python_data.get('id', None) # Get 'id' from the python_data

        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu) # converting pythond data to complex data
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type = 'application/json') # send back the response to the FE
            except Student.DoesNotExist:
                error_msg = 'Id does not exist'
                raise Exception(error_msg)
        else:
            # else return whole student object - return all the data
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')

    # post data
    def post(self, request, *args, **kwargs):
        # since we are getting data in JSON format from front end
        # first we have to convert it into pythondata to complex-data and then add to database
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

    # udapte - put data
    def put(self, request, *args, **kwargs):
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=python_data, partial=True) # updating partially only. Updating some data, not all of the data
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

    # delete data
    def delete(self, request, *args, **kwargs):
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {'msg': 'Data Deleted!'}

            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')

            # instead of using above 2 lines, we can use single line of code using JsonResponse()
            # If the data is not in "dict" then "safe=False"
            return JsonResponse(res, safe=False)
        except Student.DoesNotExist:
            error_msg = 'Id does not exist'
            raise Exception(error_msg)
        