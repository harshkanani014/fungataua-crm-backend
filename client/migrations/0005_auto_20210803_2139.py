# Generated by Django 3.2.5 on 2021-08-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20210803_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='emergency_phone_number',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client_service_records',
            name='refered_by',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]