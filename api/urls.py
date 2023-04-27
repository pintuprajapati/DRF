from django.urls import path
from api import views

urlpatterns = [
    path('studentapi/', views.StudentListCreate.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()), # for browsable API testing - we have to mention pk in urls.py
]