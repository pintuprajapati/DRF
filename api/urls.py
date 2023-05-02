from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

"""
- First Create a Route() object and then register the class with Route()
- Connect Router() object with program and then Route() will take care of routing automatically

- Because of this Router, we won't have to use 'studentapi/<int:pk>/', this 'pk' will be handled automatically
"""

# Creating Router Object
router = DefaultRouter()

# Register class with Router
router.register('studentapi', views.StudentModelViewSet, basename='student')
router.register('studentapi-readonly', views.StudentReadOnlyModelViewSet, basename='readonly')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')), # To enable Login, Logout option in Browsable API
    path('gettoken/', obtain_auth_token),
]
"""
We can get/create the token by hitting this url from cmd:
http POST http://127.0.0.1:8000/api/gettoken/ username="admin" password="admin"

above command runs because of 'pip install httpie'

Output will be:
{
    "token": "a33c619b47add6c1ab66b50569031d1fffb89a77"
}
"""

