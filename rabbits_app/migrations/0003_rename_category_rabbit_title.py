# Generated by Django 4.0.3 on 2022-10-29 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rabbits_app', '0002_remove_rabbit_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rabbit',
            old_name='category',
            new_name='title',
        ),
    ]