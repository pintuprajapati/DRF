from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    """
    BasePermission provides 2 permissions
        1. has_permission
        2. has_object_permission

    return: boolean
    """
    def has_permission(self, request, view):
        # if it's a GET request then User will be able to access the API otherwise user won't have permission to access
        if request.method == "GET":
            return True
        # if request.method == "POST":
        #     return True
        return False