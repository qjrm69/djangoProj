# Generated by Django 4.0.3 on 2022-03-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detectme', '0011_auto_20220320_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traffic',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='time',
            field=models.TimeField(),
        ),
    ]
