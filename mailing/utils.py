from time import sleep

def send_sms(phone_number: str, text: str) -> None:
    """
    Имитация отправки сообщения на телефон клиента в виде задержки
    """
    
    sleep(1)
    print(text)
