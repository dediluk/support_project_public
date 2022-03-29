from email.policy import default
from os import read
from tickets.models import Ticket, Message
from rest_framework import serializers

class TicketDetailsForUserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    title = serializers.CharField(read_only=True)
    class Meta:
        model = Ticket
        # fields = ('title', 'status', 'user')
        fields = ('id', 'title','user', 'status',)


class TicketDetailsForStaffSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Ticket
        fields = ('status', 'user')
        

class TicketListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    class Meta:
        model = Ticket
        fields = ('id', 'title', 'user', "status",)        
     
      
class MessageDetailsSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    # ticket = serializers.Fo(slug_field='ticket', read_only=True)
    
    class Meta:
        model = Message
        fields = ('text', 'user')
     
        
class MessageListByTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'