from rest_framework.permissions import BasePermission


class IsAdminOrStudent(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff or
                    request.user and request.user == obj)


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsAdminOrTeacher(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff or
                    request.user and request.user.is_teacher)
