from django.urls import path
from .views import StudentAPI

urlpatterns = [
    path('studentapi/', StudentAPI.as_view()),
    path('studentapi/<int:pk>/', StudentAPI.as_view(), name="studentAPI"), # for browsable API testing - we have to mention pk in urls.py
]