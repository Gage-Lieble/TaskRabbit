# Generated by Django 4.0.3 on 2022-11-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rabbits_app', '0003_alter_rabbit_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rabbit',
            name='links',
            field=models.CharField(max_length=999999),
        ),
    ]
