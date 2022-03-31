from django.urls import path
from .api import RegisterApi


urlpatterns = [
      path('api/register', RegisterApi.as_view()),
]
