from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly


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
    # IsAuthenticated - Whether user is admin or not, doesn't matter. If user is registered then user can access the API
    authentication_classes = [SessionAuthentication] # adding SessionAuthentication to this API - It uses Django's default session backend for authentication
    # permission_classes = [IsAuthenticated] # only authenticated users are allowed to access this API (User ID and Password needed)
    # permission_classes = [IsAdminUser] # only admins are allowed to access this API (IsStaff should be True)
    # permission_classes = [AllowAny] # Anyone can access this API
    permission_classes = [IsAuthenticatedOrReadOnly] # Will get access of API if Authenticated or will be able to "read only"

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ReadOnlyModelViewSet class inherits from GenericAPIView
    Actions provided by ReadOnlyModelViewSet class are
        - list()
        - retrieve()
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Overwriting Global Default BasicAuthentication and Permission Class (from settings.py)
    authentication_classes = [BasicAuthentication] # adding BasicAuthentication to this API
    permission_classes = [AllowAny] # Anyone can access this API