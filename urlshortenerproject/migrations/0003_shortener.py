# Generated by Django 4.1.2 on 2022-11-02 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortenerproject', '0002_remove_staff_email_remove_staff_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('long_url', models.URLField()),
                ('short_url', models.CharField(blank=True, max_length=20, unique=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urlshortenerproject.staff')),
            ],
        ),
    ]
