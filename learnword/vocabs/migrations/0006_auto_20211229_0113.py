# Generated by Django 2.1 on 2021-12-29 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('vocabs', '0005_auto_20211223_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Learningweb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webname', models.CharField(max_length=30, verbose_name='webname')),
                ('webaddr', models.CharField(max_length=100, verbose_name='webaddr')),
                ('user', models.ForeignKey(null=True, on_delete='models.CASCADE', to='users.User')),
            ],
        ),
        migrations.AlterField(
            model_name='vocab',
            name='audio',
            field=models.ImageField(upload_to='audio/'),
        ),
        migrations.AlterField(
            model_name='vocab',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
