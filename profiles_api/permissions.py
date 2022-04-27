from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ o usuario edita seu proprio perfil"""

    def has_objetc_permission(self, request, view, obj):
        """permite que o usuario edite seu proprio perfil"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
