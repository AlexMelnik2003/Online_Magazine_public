from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsEditor(permissions.BasePermission):
    def has_permission(self, request, view):
        # Проверка, аутентифицирован ли пользователь
        if not request.user.is_authenticated:
            raise PermissionDenied("Доступ запрещён: пользователь не аутентифицирован.")

        # Проверка, существует ли профиль пользователя
        if not hasattr(request.user, 'profile'):
            raise PermissionDenied("Доступ запрещён: у пользователя нет профиля.")

        # Проверка роли пользователя
        if request.user.profile.role == 'editor':
            raise PermissionDenied("Доступ запрещён: необходимы права редактора.")

        return True
