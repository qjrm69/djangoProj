# Generated by Django 4.0.3 on 2022-03-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detectme', '0014_alter_traffic_date_alter_traffic_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traffic',
            name='date',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='time',
            field=models.TimeField(),
        ),
    ]
