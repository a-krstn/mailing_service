from rest_framework import serializers

from .models import Mailing, Client, Message


class MailingSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели рассылки
    """

    class Meta:
        model = Mailing
        fields = (
            'id',
            'start_time',
            'end_time',
            'filters',
            'text',
            )
        
    def validate(self, attrs):
        print(type(attrs['start_time']))
        if attrs['start_time'] >= attrs['end_time']:
            raise serializers.ValidationError("Время окончания рассылки должно быть больше времени запуска.")
        return attrs
