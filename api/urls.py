from django.urls import path
from .views import student_api

urlpatterns = [
    path('studentapi/', student_api),
]