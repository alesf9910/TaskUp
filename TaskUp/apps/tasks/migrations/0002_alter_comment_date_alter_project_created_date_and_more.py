# Generated by Django 4.1.5 on 2023-05-06 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 6, 3, 16, 53, 9566)),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 6, 3, 16, 53, 1618)),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 6, 3, 16, 53, 2570)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 6, 3, 16, 53, 2570)),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 6, 3, 16, 53, 7570)),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 6, 3, 16, 53, 7570)),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 6, 3, 16, 53, 7570)),
        ),
    ]