# Generated by Django 4.0.3 on 2022-10-29 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rabbits_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rabbit',
            name='links1',
        ),
        migrations.RemoveField(
            model_name='rabbit',
            name='links2',
        ),
        migrations.RemoveField(
            model_name='rabbit',
            name='links3',
        ),
        migrations.RemoveField(
            model_name='rabbit',
            name='links4',
        ),
        migrations.RemoveField(
            model_name='rabbit',
            name='links5',
        ),
    ]