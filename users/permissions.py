from rest_framework.permissions import BasePermission


class IsEmployerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            profile = getattr(request.user, 'user_profile', None)
            return profile.exists() and profile.first().is_employer
        return False


class IsEmployeePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            profile = getattr(request.user, 'user_profile', None)
            return profile.exists() and profile.first().is_employee
        return False
