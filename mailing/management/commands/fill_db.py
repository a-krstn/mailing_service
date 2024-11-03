from django.core.management.base import BaseCommand

from mailing.models import Mailing, Client, Message


class Command(BaseCommand):
    """
    Класс для заполнения БД (6 клиентов)
    """

    def handle(self, *args, **options):
        # Удаление всех существующих записей из БД
        Mailing.objects.all().delete()
        Client.objects.all().delete()
        Message.objects.all().delete()

        # Создание 6 клиентов
        # Создание 3 клиентов с одинаковым кодом оператора и разными тегами (оператором)
        client_1 = Client(phone_number=f'79001234567', operator_code=f'900', tag='МТС')
        client_2 = Client(phone_number=f'79001234568', operator_code=f'900', tag='Мегафон')
        client_3 = Client(phone_number=f'79001234569', operator_code=f'900', tag='Т2')

        # Создание ещё 3 клиентов с разными кодами операторов и разными тегами (операторами)
        client_4 = Client(phone_number=f'79011234567', operator_code=f'901', tag='МТС')
        client_5 = Client(phone_number=f'79021234567', operator_code=f'902', tag='Мегафон')
        client_6 = Client(phone_number=f'79031234567', operator_code=f'903', tag='Т2')

        Client.objects.bulk_create(
            [
                client_1,
                client_2,
                client_3,
                client_4,
                client_5,
                client_6
            ]
        )
        


