# Generated by Django 5.0.1 on 2024-01-07 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('sender', models.CharField(max_length=255)),
            ],
        ),
    ]
