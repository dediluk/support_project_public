from django.urls import path

from account.api import RegisterApi

urlpatterns = [
      path('register', RegisterApi.as_view()),
]
