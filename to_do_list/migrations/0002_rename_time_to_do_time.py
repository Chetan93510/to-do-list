# Generated by Django 5.1 on 2024-08-28 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='to_do',
            old_name='Time',
            new_name='time',
        ),
    ]
