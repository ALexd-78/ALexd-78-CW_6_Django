from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Blog(models.Model):
    heading = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='blogs/', verbose_name='Изображение', **NULLABLE)
    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.heading}'


    class Meta:
        '''Класс мета-настроек'''
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
        ordering = ('heading',)
