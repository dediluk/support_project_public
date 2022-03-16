from tickets.models import Ticket, Message
from rest_framework import serializers

class TicketDetailsForUserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    class Meta:
        model = Ticket
        fields = ('title', 'status', 'user')


class TicketDetailsForStaffSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Ticket
        fields = ('title', 'status', 'user')
        

class TicketListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('id', 'title', 'user', "status",)        
     
      
class MessageDetailsSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    
    class Meta:
        model = Message
        fields = '__all__'
     
        
class MessageListByTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'