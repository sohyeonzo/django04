# Generated by Django 4.0.3 on 2022-05-04 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_alter_board_pubdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 10, 47, 50, 880502)),
        ),
    ]
