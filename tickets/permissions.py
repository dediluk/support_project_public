from rest_framework.permissions import BasePermission, SAFE_METHODS
from tickets.models import Ticket

class IsOwnerOfTicketPermission(BasePermission):
   def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
    
    
class IsOwnerOfTicketForMessagePermission(BasePermission):
    def has_permission(self, request, view):
        return Ticket.objects.get(pk=view.kwargs['pk']).user == request.user


class IsTicketClosedPermission(BaseException):
    def has_object_permission(self, request, view, obj):
        if Ticket.objects.get(pk=view.kwargs['pk']).status in('Closed', 'Freeze'):
            return False
        return 1

    def has_permission(self, request, view):
        if Ticket.objects.get(pk=view.kwargs['pk']).status in('Closed', 'Freeze'):
            return False
        return 1