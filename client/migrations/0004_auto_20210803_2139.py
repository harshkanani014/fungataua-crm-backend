# Generated by Django 3.2.5 on 2021-08-03 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20210801_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_images',
            name='date_of_add',
            field=models.DateField(default=datetime.date(2021, 8, 3)),
        ),
        migrations.AlterField(
            model_name='client_service_records',
            name='date_of_visit',
            field=models.DateField(default=datetime.date(2021, 8, 3)),
        ),
    ]
