from datetime import datetime

from django.shortcuts import render
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Mailing
from .serializers import MailingSerializer
from .tasks import send_mailing


class MailingListCreateAPIView(generics.ListCreateAPIView):
    """
    Представление для отображения списка рассылок и их создания
    """

    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        current_time = timezone.now()

        # запрет на создание просроченной рассылки
        if serializer.validated_data['end_time'] < current_time:
            return Response(
                {"error": "Время окончания рассылки меньше текущего времени."},
                status=status.HTTP_400_BAD_REQUEST
                )
        
        serializer.save()

        # прямой запуск рассылки, если время запуска созданной рассылки меньше текущего времени
        if datetime.fromisoformat(serializer.data['start_time']) <= current_time:
            send_mailing.delay(serializer.data['id'])

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
