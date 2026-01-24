
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsProjectOwner(BasePermission):


    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsTaskProjectOwner(BasePermission):
   

    def has_object_permission(self, request, view, obj):
        return obj.project.owner == request.user
