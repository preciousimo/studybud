# Generated by Django 3.2.10 on 2022-03-05 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
