from django.urls import path
from tickets.views import *

urlpatterns = [
    path('api/v1/ticket/create', TicketCreateView.as_view()),
    path('api/v1/ticket/detail/<int:pk>', TicketDetailsView.as_view()),
    path('api/v1/ticket/all', TicketListView.as_view()),
    
    path('api/v1/ticket/detail/<int:pk>/message/create', MessageCreateView.as_view()),
    path('api/v1/ticket/detail/<int:pk>/message/all', MessageByTicketListView.as_view()),
]
