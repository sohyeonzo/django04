# Generated by Django 4.0.3 on 2022-04-26 00:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 26, 0, 22, 18, 430768, tzinfo=utc)),
        ),
    ]
