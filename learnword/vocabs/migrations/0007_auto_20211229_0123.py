# Generated by Django 2.1 on 2021-12-29 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabs', '0006_auto_20211229_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocab',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
