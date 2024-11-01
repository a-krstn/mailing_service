from django.contrib import admin

from .models import Mailing, Client, Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'start_time', 'end_time')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'operator_code', 'tag')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_time', 'mailing', 'client')
