# Generated by Django 2.2.2 on 2019-06-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kto', '0005_auto_20190624_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(),
        ),
    ]
