from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their profile only when authorized"""

    def has_object_permission(self,request,view,obj):
        """check if the user has permission"""
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id==request.user.id