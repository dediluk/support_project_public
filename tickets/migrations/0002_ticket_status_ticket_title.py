# Generated by Django 4.0.3 on 2022-03-14 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(choices=[(1, 'Завершен'), (2, 'Незавершен'), (3, 'Заморожен')], default=1, verbose_name='Статус тикета'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='title',
            field=models.CharField(default=1, max_length=120, verbose_name='Тема'),
            preserve_default=False,
        ),
    ]