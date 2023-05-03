from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

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

    # JWT Authentication
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Will return access and refresh token (token time limit=5 min)
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'), # It will give you new fresh token (token time limit = 1 day)
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'), # Checks whether token is valid or not
]

# Read "README.md" file for more details on how to test this API in CMD and POSTMAN

