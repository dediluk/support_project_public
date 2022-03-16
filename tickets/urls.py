from django.urls import path
from tickets.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/v1/ticket/all', TicketListView.as_view()),
    path('api/v1/ticket/create', TicketCreateView.as_view()),
    path('api/v1/ticket/detail/<int:pk>', TicketDetailsView.as_view()),
    path('api/v1/ticket/detail/<int:pk>/change', TicketChangeView.as_view()),
    path('api/v1/ticket/detail/<int:pk>/message/create', MessageCreateView.as_view()),
    path('api/v1/ticket/detail/<int:pk>/message/all', MessageListByTicketListView.as_view()),
]
