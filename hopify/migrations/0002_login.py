# Generated by Django 4.0.2 on 2022-03-24 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopify', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
