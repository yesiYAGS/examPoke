# Generated by Django 3.2.9 on 2021-12-11 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='alias',
        ),
    ]
