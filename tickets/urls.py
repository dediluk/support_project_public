from django.urls import path
from tickets.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from tickets.views import TicketViewSet
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register(r'tickets', TicketViewSet, basename='tickets')
# router.register(r'tickets/<int:pk>', TicketViewSet, basename='ticket_details')
urlpatterns = router.urls


# urlpatterns = [
#     path('api/v1/ticket/all', TicketListView.as_view()),
#     path('api/v1/ticket/create', TicketCreateView.as_view()),
#     path('api/v1/ticket/detail/<int:pk>', TicketDetailsView.as_view()),
#     path('api/v1/ticket/detail/<int:pk>/change', TicketChangeView.as_view()),
#     path('api/v1/ticket/detail/<int:pk>/message/create', MessageCreateView.as_view()),
#     path('api/v1/ticket/detail/<int:pk>/message/all', MessageListByTicketListView.as_view()),
# ]
