from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tickets import serializers
from tickets.serializers import *
from tickets.models import Ticket, Message

class TicketDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketDetailsSerializer
    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated,)


class TicketCreateView(generics.CreateAPIView):
    serializer_class = TicketDetailsSerializer
    
    

class TicketListView(generics.ListAPIView):
    serializer_class = TicketListSerializer
    queryset = Ticket.objects.all()
    
    
class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageDetailsSerializer
    
class MessageByTicketListView(generics.ListAPIView):
    serializer_class = MessageByTicketSerializer

    
    def get_queryset(self):
        queryset = Message.objects.filter(ticket=self.kwargs['pk'])
        return queryset