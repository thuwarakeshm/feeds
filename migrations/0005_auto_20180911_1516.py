# Generated by Django 2.1.1 on 2018-09-11 15:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20180911_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 15, 16, 15, 166855, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 15, 16, 15, 167789, tzinfo=utc)),
        ),
    ]
