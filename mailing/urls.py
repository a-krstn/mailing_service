from django.urls import path

from .views import MailingListCreateAPIView


urlpatterns = [
    path('mailings/', MailingListCreateAPIView.as_view(), name='mailings'),
]