from rest_framework.permissions import BasePermission

from users.models import User


class IsOwnerSelection(BasePermission):
    message = "Вы не являетесь владельцем данной подборки"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsOwnerAdOrStaff(BasePermission):
    message = "Вы не являетесь владельцем данного объявления или администратором."

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author_id or request.user.role in [User.MODERATOR, User.ADMIN]:
            return True
        return False
