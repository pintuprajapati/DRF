from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

"""
- First Create a Route() object and then register the class with Route()
- Connect Router() object with program and then Route() will take care of routing automatically

- Because of this Router, we won't have to use 'studentapi/<int:pk>/', this 'pk' will be handled automatically
"""

# Creating Router Object
router = DefaultRouter()

# Register class with Router
router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]