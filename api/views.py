from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# CRUD Operations will be done using only these 2 APIViews
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
