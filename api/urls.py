from django.urls import path
from .views import student_detail, student_list, student_create

urlpatterns = [
    path('stuinfo/<int:pk>/',student_detail),
    path('stuinfo/',student_list),
    path('stucreate/', student_create)
]