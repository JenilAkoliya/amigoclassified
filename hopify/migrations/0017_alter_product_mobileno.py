# Generated by Django 4.0.2 on 2022-03-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopify', '0016_alter_product_mobileno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mobileno',
            field=models.FloatField(),
        ),
    ]
