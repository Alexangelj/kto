# Generated by Django 2.2.2 on 2019-06-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kto', '0002_auto_20190620_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
