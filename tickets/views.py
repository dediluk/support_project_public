from urllib import request
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from tickets.permissions import IsOwnerOfTicketForMessagePermission, IsOwnerOfTicketPermission, IsTicketClosedPermission
from tickets import serializers
from tickets.serializers import *
from tickets.models import Ticket, Message


class TicketViewSet(viewsets.ViewSet):
    
    def list(self, request):
        if request.user.is_staff:
            queryset = Ticket.objects.all().only('id', 'title', 'user', "status",)
        else:
            queryset = Ticket.objects.filter(user=request.user)
        print()
        serializer_class = TicketListSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)
    

    @action(detail=True, methods=['get'], permission_classes = [IsOwnerOfTicketPermission,], url_path='details')
    def retrive(self, request, pk=None):
        queryset = Ticket.objects.all()
        ticket = get_object_or_404(queryset, pk=pk)
        serializer = TicketDetailsForUserSerializer(ticket)
        return Response(serializer.data)
    
    def get_serializer_class(self):
        print('тут берется сериалайзер', self.action)
        if self.action == 'list':
            return TicketListSerializer
        elif self.action == 'retrive':
            return TicketDetailsForUserSerializer
        return super().get_serializer_class()
    
    
    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     if self.action == 'list':
    #         print('perm of list')
    #         permission_classes = [IsAuthenticated,]
    #     else:
    #         print('perm of else')
    #         permission_classes = [IsAdminUser|IsOwnerOfTicketPermission]
    #     return [permission() for permission in permission_classes]

# class TicketDetailsView(generics.RetrieveAPIView):
#     serializer_class = TicketDetailsForUserSerializer
#     queryset = Ticket.objects.all()
#     permission_classes = (IsAuthenticated, IsOwnerOfTicketPermission)

#     def get_serializer_class(self):
#         if self.request.user.is_staff:
#             return TicketDetailsForStaffSerializer
 
#         return super(TicketDetailsView, self).get_serializer_class()


# class TicketChangeView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TicketDetailsForStaffSerializer
#     queryset = Ticket.objects.all()
#     permission_classes = (IsAdminUser,)


# class TicketCreateView(generics.CreateAPIView):
#     serializer_class = TicketDetailsForUserSerializer
#     permission_classes = (IsAuthenticated,)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)  


# class TicketListView(generics.ListAPIView):
#     serializer_class = TicketListSerializer
#     permission_classes = (IsAuthenticated,)
    
#     def get_queryset(self):
#         if self.request.user.is_staff:
#             return Ticket.objects.all()
#         else:
#             return Ticket.objects.filter(user=self.request.user)
    
    
# class MessageCreateView(generics.CreateAPIView):
#     serializer_class = MessageDetailsSerializer
#     permission_classes = (IsAdminUser|IsOwnerOfTicketForMessagePermission, IsTicketClosedPermission)

#     def perform_create(self, serializer):
#         ticket = Ticket.objects.get(pk=self.kwargs['pk'])
#         serializer.save(user=self.request.user, ticket=ticket)

    

# class MessageListByTicketListView(generics.ListAPIView):
#     serializer_class = MessageListByTicketSerializer
#     permission_classes = (IsAdminUser|IsOwnerOfTicketForMessagePermission, )
    
#     def get_queryset(self):
#         queryset = Message.objects.filter(ticket=self.kwargs['pk'])
#         return queryset