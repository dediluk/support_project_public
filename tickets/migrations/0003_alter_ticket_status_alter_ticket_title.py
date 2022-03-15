# Generated by Django 4.0.3 on 2022-03-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ticket_status_ticket_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(choices=[(1, 'Незавершен'), (2, 'Завершен'), (3, 'Заморожен')], verbose_name='Статус тикета'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=120, unique=True, verbose_name='Тема'),
        ),
    ]