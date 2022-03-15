from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from tickets.permissions import IsOwnerPermission
from tickets import serializers
from tickets.serializers import *
from tickets.models import Ticket, Message

class TicketDetailsView(generics.RetrieveAPIView):
    serializer_class = TicketDetailsForUserSerializer
    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerPermission)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return TicketDetailsForStaffSerializer

        return super(TicketDetailsView, self).get_serializer_class()

class TicketChangeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketDetailsForStaffSerializer
    queryset = Ticket.objects.all()
    permission_classes = (IsAdminUser,)

class TicketCreateView(generics.CreateAPIView):
    serializer_class = TicketDetailsForUserSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  

class TicketListView(generics.ListAPIView):
    serializer_class = TicketListSerializer
    queryset = Ticket.objects.all()
    
    
class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageDetailsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class MessageByTicketListView(generics.ListAPIView):
    serializer_class = MessageByTicketSerializer

    
    def get_queryset(self):
        queryset = Message.objects.filter(ticket=self.kwargs['pk'])
        return queryset