# Generated by Django 4.0.2 on 2022-03-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopify', '0019_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pricing',
            field=models.IntegerField(default='00'),
        ),
    ]
