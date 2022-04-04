from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from tickets.models import Message, Ticket
from tickets.permissions import (IsOwnerOfTicketForMessagePermission,
                                 IsOwnerOfTicketPermission)
from tickets.serializers import (MessageDetailsSerializer,
                                 TicketDetailsForStaffSerializer,
                                 TicketDetailsForUserSerializer,
                                 TicketListSerializer)


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketListSerializer
    queryset = Ticket.objects.all().order_by('-id')

    def list(self, request):
        queryset = Ticket.objects.all()
        if request.user.is_staff:
            queryset = Ticket.objects.all().only('id', 'title', 'user', "status",).order_by('-id')
        else:
            queryset = Ticket.objects.filter(user=request.user).order_by('-id')
        serializer_class = TicketListSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return TicketListSerializer
        elif self.action == 'update':
            if self.request.user.is_staff:
                return TicketDetailsForStaffSerializer
            else:
                return TicketDetailsForUserSerializer
        elif self.action == 'destroy':
            return TicketDetailsForUserSerializer
        elif self.action == 'retrive':
            return TicketDetailsForUserSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'update' or self.action == 'partial_update' or self.action == 'retrieve':
            permission_classes = [IsAdminUser | IsOwnerOfTicketPermission, ]
        else:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageDetailsSerializer
    queryset = Message.objects.all()

    def list(self, request, pk1: int):
        queryset = Message.objects.filter(ticket=Ticket.objects.get(id=pk1)).order_by('date')
        serializer_class = MessageDetailsSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, ticket=Ticket.objects.get(id=self.kwargs['pk1']))

    def get_permissions(self):
        if self.action in ('list', 'create'):
            permission_classes = [IsAdminUser | IsOwnerOfTicketForMessagePermission]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'retrieve':
            permission_classes = [IsOwnerOfTicketForMessagePermission, ]
        else:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]
