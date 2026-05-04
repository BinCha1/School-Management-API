from rest_framework.permissions import BasePermission


class IsPrincipalUser(BasePermission):
    """Allow access only to user with Principal role"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "PRINCIPAL"


class IsTeacherUser(BasePermission):
    """Allow access only to user with Teacher role"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "TEACHER"


class IsStudentUser(BasePermission):
    """Allow access only to user with Student role"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "STUDENT"


class IsTeacherOrPrincipal(BasePermission):
    """Allow access only to user with Teacher or Principal role. Useful for Management level API"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == [
            "TEACHER",
            "PRINCIPAL",
        ]
