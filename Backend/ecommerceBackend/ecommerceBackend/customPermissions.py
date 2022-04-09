
from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):

    # edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        
        return True
