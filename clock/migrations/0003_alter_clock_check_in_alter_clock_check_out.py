# Generated by Django 5.0 on 2023-12-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock', '0002_remove_clock_check_in_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clock',
            name='check_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='clock',
            name='check_out',
            field=models.DateTimeField(),
        ),
    ]
