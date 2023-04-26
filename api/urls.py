from django.urls import path
from .views import LCStudentAPI, RUDStudentAPI

urlpatterns = [
    path('studentapi/', LCStudentAPI.as_view()),
    path('studentapi/<int:pk>/', RUDStudentAPI.as_view()), # for browsable API testing - we have to mention pk in urls.py
]