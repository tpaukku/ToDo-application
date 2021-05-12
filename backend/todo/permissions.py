from rest_framework import permissions


# Restrict access to users own todo-items
class IsTodoAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
