# Generated by Django 4.0.2 on 2022-03-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopify', '0009_rename_mypassword_mylogin_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='editprofile',
            name='phone',
            field=models.IntegerField(default='0091'),
        ),
    ]
