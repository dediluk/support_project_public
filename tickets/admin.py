from django.contrib import admin

from tickets.models import Message, Ticket

admin.site.register(Ticket)
admin.site.register(Message)
