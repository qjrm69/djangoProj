# Generated by Django 3.2.12 on 2022-03-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detectme', '0010_auto_20220320_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traffic',
            name='date',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='time',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
