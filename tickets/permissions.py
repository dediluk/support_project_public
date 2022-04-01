from rest_framework.permissions import BasePermission

from tickets.models import Ticket


class IsOwnerOfTicketPermission(BasePermission):
    def has_permission(self, request, view):
        return Ticket.objects.get(pk=view.kwargs['pk']).user == request.user


class IsOwnerOfTicketForMessagePermission(BasePermission):
    def has_permission(self, request, view):
        return Ticket.objects.get(pk=view.kwargs['pk1']).user == request.user
