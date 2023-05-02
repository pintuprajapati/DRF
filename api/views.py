from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .custompermissions import MyPermission

class StudentModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet class inherits from GenericAPIView
    Actions provided by ModelViewSet class are
        - list()
        - retrieve()
        - create()
        - update()
        - partial_update()
        - destroy()
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Authentication and Permission
    authentication_classes = [SessionAuthentication] # adding SessionAuthentication to this API - It uses Django's default session backend for authentication
    permission_classes = [MyPermission] # Custom Permission Class

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ReadOnlyModelViewSet class inherits from GenericAPIView
    Actions provided by ReadOnlyModelViewSet class are
        - list()
        - retrieve()
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    