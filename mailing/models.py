from django.db import models

from config import settings
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    '''Модель клиент'''
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    email = models.EmailField(max_length=150, unique=True, verbose_name='почта', **NULLABLE)
    comment = models.TextField(max_length=400, verbose_name='комментарий', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='активный')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('last_name',)

class Message(models.Model):
    '''Модель сообщения рассылки'''
    name = models.CharField(max_length=150, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')
    is_publication = models.BooleanField(default=True, verbose_name='Опубликовано')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    def delete(self, *args, **kwargs):
        self.is_publication = False
        self.save()

    class Meta:
        '''Класс мета-настроек'''
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('name',)  # сортировка, '-name' - сортировка в обратном порядке


class SetMessage(models.Model):
    '''Модель настройки рассылки'''
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='рассылка', null=True)
    mailing_time = models.DateTimeField(auto_now_add=True, verbose_name='время рассылки')
    # frequency = models.Model(verbose_name='периодичность')
    # status = models.Model(verbose_name='статус рассылки')


    def __str__(self):
        return f'{self.name}, {self.frequency}, {self.status}'

    class Meta:
        '''Класс мета-настроек'''
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылки'
        ordering = ('mailing_time',)  # сортировка, '-name' - сортировка в обратном порядке
        # ordering = ('mailing_time', 'frequency', 'status',)  # сортировка, '-name' - сортировка в обратном порядке


class LogMessage(models.Model):
    '''Модель лога рассылки'''
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='рассылка', null=True)
    last_try = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    status_try = models.BooleanField(default=False, verbose_name='статус попытки')
    # server_response = models.Model(verbose_name='ответ почтового сервера')


    def __str__(self):
        return f'{self.msg}, {self.last_try}, {self.status_try}'

    class Meta:
        '''Класс мета-настроек'''
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылки'
        ordering = ('status_try',)  # сортировка, '-name' - сортировка в обратном порядке




