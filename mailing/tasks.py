from django.utils import timezone

from celery import shared_task

from .models import Mailing, Client, Message
from .utils import send_sms
from services import redis_services


@shared_task
def send_mailing(mailing_id: int) -> None:
    """
    Задача, отправляющая рассылку клиентам
    """
    
    # получение рассылки из БД
    mailing = Mailing.objects.get(id=mailing_id)
    
    # получение всех клиентов из БД
    clients = Client.objects.all()

    # фильтрация клиентов по фильтрам рассылки
    if mailing.filters:
        if 'operator_code' in mailing.filters:
            clients = clients.filter(operator_code=mailing.filters['operator_code'])

        if 'tag' in mailing.filters:
            clients = clients.filter(tag=mailing.filters['tag'])

    # отправка рассылки клиентам с проверкой времени её окончания
    for client in clients:
        current_time = timezone.now()
        if current_time <= mailing.end_time:
            send_sms(client.phone_number, mailing.text)
            Message.objects.create(mailing=mailing, client=client)
        else:
            break
    
    # добавить рассылку в список выполненных
    redis_services.add_to_list('mailing_ids', mailing.pk)


@shared_task
def check_and_start_mailings() -> None:
    """
    Периодическая задача, запускающая рассылки
    """

    # получение текущего времени
    current_time = timezone.now()

    # получение списка идентификаторов выполненных рассылок
    completed_mailing_ids = redis_services.get_list('mailing_ids')
    print(completed_mailing_ids)

    # получение рассылок из БД, у которых время запуска меньше текущего времени, исключая уже выполненные рассылки
    mailings_to_start = Mailing.objects.filter(start_time__lte=current_time).exclude(pk__in=completed_mailing_ids)

    # запуск рассылки с проверкой времени окончания
    if mailings_to_start:
        print(mailings_to_start)
        for mailing in mailings_to_start:
            if timezone.now() <= mailing.end_time:
                send_mailing.delay(mailing.id)
    else:
        print('Нет рассылок для выполнения')
