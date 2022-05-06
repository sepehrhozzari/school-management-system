from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsTeacherOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.user.is_teacher or\
                request.user.is_authenticated and request.user.is_staff:
            return True
        else:
            return False
