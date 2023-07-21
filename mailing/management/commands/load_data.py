import json

from django.core.management import BaseCommand, call_command

from blog.models import Blog
from mailing.models import Client, Message


class Command(BaseCommand):

    def handle(self, *args, **options):

        # удаление данных из таблицы Blog
        Blog.objects.all().delete()
        # удаление данных из таблицы Client
        Client.objects.all().delete()
        # удаление данных из таблицы Message
        Message.objects.all().delete()

        # наполнение таблицы Blog из json-файла
        call_command('loaddata', 'blog.json')
        # наполнение таблицы Client из json-файла
        call_command('loaddata', 'client.json')
        # наполнение таблицы Message из json-файла
        call_command('loaddata', 'message.json')

