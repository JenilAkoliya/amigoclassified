# Generated by Django 4.0.2 on 2022-03-24 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hopify', '0004_rename_mypassword_login_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='Mylogin',
        ),
    ]
