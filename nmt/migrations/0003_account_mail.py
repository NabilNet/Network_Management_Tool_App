# Generated by Django 4.2 on 2024-05-05 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmt', '0002_alter_account_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='mail',
            field=models.EmailField(default='admin@gmail.com', max_length=254),
        ),
    ]
