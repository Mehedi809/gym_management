from rest_framework import permissions

class IsAdminOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['ADMIN', 'MANAGER']

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, obj):
        if request.user.role == 'ADMIN':
            return True
        return obj == request.user