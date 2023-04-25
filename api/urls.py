from django.urls import path
from .views import student_api

urlpatterns = [
    path('studentapi/',student_api),
    # path('studentapi/<int:pk>/', student_api, name="student_api"), # for browsable API testing - we have to mention pk in urls.py
]