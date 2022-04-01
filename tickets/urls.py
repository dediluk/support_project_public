from rest_framework.routers import SimpleRouter

from tickets.views import MessageViewSet, TicketViewSet

router = SimpleRouter()
router.register(r'tickets', TicketViewSet, basename='tickets')
router.register(r'tickets/(?P<pk1>\d+)/messages', MessageViewSet, basename='messages')
urlpatterns = router.urls
