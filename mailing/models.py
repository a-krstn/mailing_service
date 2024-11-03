from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Mailing(models.Model):
    """
    Модель рассылки
    """

    text = models.TextField(
        verbose_name='Текст рассылки'
        )
    start_time = models.DateTimeField(
        verbose_name='Дата и время запуска рассылки'
        )
    end_time = models.DateTimeField(
        verbose_name='Дата и время окончания рассылки'
        )
    filter = models.JSONField(
        null=True,
        verbose_name='Фильтр свойств клиентов'
        )
    

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


    def __str__(self):
        """
        Строковое представление объекта рассылки
        """

        return f'Рассылка №{self.pk}'


class Client(models.Model):
    """
    Модель клиента
    """

    phone_number = models.CharField(
        max_length=11,
        unique=True,
        verbose_name='Номер телефона'
        )
    operator_code = models.CharField(
        max_length=3,
        verbose_name='Код мобильного оператора'
        )
    tag = models.CharField(
        max_length=30,
        verbose_name='Произвольная метка'
        )


    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


    def __str__(self):
        """
        Строковое представление объекта клиента
        """

        return f'{self.pk}:{self.phone_number}'
    
    def clean(self):
        super().clean()
        if not self.phone_number.startswith('7'):
            raise ValidationError('Номер телефона должен начинаться с цифры 7.')
        if not self.phone_number.isdigit():
            raise ValidationError('Номер телефона должен состоять только из цифр.')


class Message(models.Model):
    """
    Модель сообщения
    """

    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
        )
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        verbose_name='Рассылка',
        related_name='messages'
        )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='Клиент',
        related_name='messages'
        )
    

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    
    def __str__(self):
        """
        Строковое представление модели сообщения
        """

        return f'Сообщение №{self.pk}'
