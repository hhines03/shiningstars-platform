from rest_framework import permissions

class IsParentOfChildOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow parents of a child to view/edit it,
    or admins.
    """

    def has_object_permission(self, request, view, obj):
        #rule 1: give admin access to every permission
        if request.user.role == 'admin':
            return True
        
        #rule 2: For any other users perform a two part safety check:
        # 1. check if the object has the 'parent' attribute
        # 2. check if that parent is the user making the request
        return hasattr(obj, 'parent') and obj.parent == request.user

        

        