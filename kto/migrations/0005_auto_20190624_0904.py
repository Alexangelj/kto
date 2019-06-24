# Generated by Django 2.2.2 on 2019-06-24 16:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kto', '0004_task_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 24, 16, 4, 20, 922099, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 24, 16, 4, 28, 98249, tzinfo=utc)),
            preserve_default=False,
        ),
    ]