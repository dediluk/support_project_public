# Generated by Django 4.0.3 on 2022-03-16 07:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0005_message_date_message_text_message_ticket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Open', 'Незавершен'),
                                            ('Closed', 'Завершен'), ('Freeze', 'Заморожен')], default='Open',
                                   max_length=30, verbose_name='Статус тикета'),
        ),
    ]
