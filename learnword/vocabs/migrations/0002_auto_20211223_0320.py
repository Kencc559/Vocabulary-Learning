# Generated by Django 2.1 on 2021-12-23 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocabs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vocab',
            old_name='user',
            new_name='user_id',
        ),
    ]