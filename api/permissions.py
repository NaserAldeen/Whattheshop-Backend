from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "This is not your cart!"

    def has_object_permission(self, request, view, obj):
        if  (obj.profile.user == request.user):
            return True
        else:
            return False