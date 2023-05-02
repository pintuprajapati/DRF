from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# for authentication and permissoins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, authentication_classes, permission_classes 

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])

# @authentication_classes([SessionAuthentication])
# @permission_classes([AllowAny])
# @permission_classes([IsAdminUser])
# @permission_classes([IsAuthenticatedOrReadOnly])

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])

# def student_api(request, pk=None): # For browsable API testing, you can uncomment this and test it
def student_api(request):
    if request.method == 'GET':
        # Here, we don't have to 'get json_data' or 'stream' or 'parse(stream)' and then get the 'id'.
        # We can directly get the 'id' as shown below
        id = request.data.get('id')
        # id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            print("➡ serializer :", serializer)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        # id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        id = request.data.get('id')
        # id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': ' Partial Data Updated!'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = request.data.get('id') # id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'Data Deleted!'}, status=status.HTTP_200_OK)
