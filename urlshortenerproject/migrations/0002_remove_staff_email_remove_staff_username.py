# Generated by Django 4.0.3 on 2022-04-21 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortenerproject', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='email',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='username',
        ),
    ]
