import redis

from django.conf import settings


redis_db = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True  # чтобы получать строки вместо байтов
)

def add_to_list(key: str, mailing_id: int) -> None:
    """
    Добавляет mailing_id в список выполненных рассылок
    """

    redis_db.rpush(key, mailing_id)


def get_list(key:str) -> None:
    """
    Выводит список выполненных рассылок
    """

    return redis_db.lrange(key, 0, -1)
