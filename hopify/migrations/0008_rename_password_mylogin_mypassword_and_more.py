# Generated by Django 4.0.2 on 2022-03-25 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hopify', '0007_editprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mylogin',
            old_name='password',
            new_name='mypassword',
        ),
        migrations.RenameField(
            model_name='mylogin',
            old_name='username',
            new_name='myusername',
        ),
    ]
