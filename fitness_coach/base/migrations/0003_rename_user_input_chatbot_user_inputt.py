# Generated by Django 4.1.3 on 2022-11-11 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_chatbot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatbot',
            old_name='user_input',
            new_name='user_inputt',
        ),
    ]