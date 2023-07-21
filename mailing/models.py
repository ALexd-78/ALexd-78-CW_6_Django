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
    '''Модель рассылки'''
    FREQUENCY = [
        ('DAY', 'раз в день'),
        ('WEEK', 'раз в неделю'),
        ('MONTH', 'раз в месяц')
    ]

    STATUS = [
        ('FINISH', 'завершена'),
        ('CREATE', 'создана'),
        ('START', 'запущена')
    ]

    time = models.TimeField(auto_now_add=True, verbose_name='Время рассылки')
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    frequency = models.CharField(max_length=100, choices=FREQUENCY, verbose_name='Периодичность')
    status = models.CharField(max_length=100, choices=STATUS, verbose_name='Статус')
    client = models.ManyToManyField(Client, verbose_name='Клиент', **NULLABLE)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name='Сообщение', **NULLABLE)
    finish_date = models.DateField(verbose_name='Дата завершения рассылки', default='2024-01-01')
    finish_time = models.TimeField(verbose_name='Время завершения рассылки', default='00:00')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('time',)

    def __str__(self):
        return f'Рассылка №{self.pk}'

    def delete(self, *args, **kwargs):
        """Функция, делающая пост не активным"""
        self.is_published = False
        self.status = 'FINISH'
        self.save()


class LogMessage(models.Model):
    '''Модель лога рассылки'''
    STATUS = [
        ('Success', 'успешно'),
        ('Failure', 'отказ')
    ]

    data_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки')
    status = models.CharField(max_length=100, choices=STATUS, verbose_name='Статус попытки')
    server_response = models.TextField(verbose_name='Ответ почтового сервера', **NULLABLE)
    mailing = models.ForeignKey(SetMessage, on_delete=models.SET_NULL, verbose_name='Рассылка', **NULLABLE)

    class Meta:
        verbose_name = 'лог отправки письма'
        verbose_name_plural = 'логи отправок писем'

    def __str__(self):
        return f'Лог {self.pk}'