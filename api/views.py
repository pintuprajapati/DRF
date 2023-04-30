from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets

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

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ReadOnlyModelViewSet class inherits from GenericAPIView
    Actions provided by ReadOnlyModelViewSet class are
        - list()
        - retrieve()
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    