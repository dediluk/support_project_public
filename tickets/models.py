from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

class Ticket(models.Model):
    title = models.CharField(verbose_name='Тема', unique=True, max_length=120)
    STATUS_TYPE = (
        ('Open', 'Незавершен'),
        ('Closed', 'Завершен'),
        ('Freeze', 'Заморожен'),
    )
    status = models.CharField(verbose_name='Статус тикета', choices=STATUS_TYPE, max_length=30)
    user = models.ForeignKey(USER, verbose_name='user', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Тикет'
        verbose_name_plural = 'Тикеты'
        
    def __str__(self):
        return self.title

class Message(models.Model):
    text = models.TextField(verbose_name='Текст сообщения')
    ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'