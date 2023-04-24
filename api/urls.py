from django.urls import path
from .views import StudentAPI

urlpatterns = [
    path('studentapi/', StudentAPI.as_view()),
]