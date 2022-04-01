from rest_framework import serializers

from tickets.models import Message, Ticket


class TicketDetailsForUserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    title = serializers.CharField(read_only=True)

    class Meta:
        model = Ticket
        fields = ('id', 'title', 'user', 'status',)


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

    class Meta:
        model = Message
        fields = ('text', 'user')
