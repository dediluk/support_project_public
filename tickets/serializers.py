from tickets.models import Ticket, Message
from rest_framework import serializers

class TicketDetailsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Ticket
        fields = '__all__'
        

class TicketListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ticket
        fields = ('id', 'title', 'user', "status")
        
      
class MessageDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        
class MessageByTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'