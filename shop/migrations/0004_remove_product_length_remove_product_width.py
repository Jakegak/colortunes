# Generated by Django 4.0.4 on 2022-05-10 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_length_product_width'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='length',
        ),
        migrations.RemoveField(
            model_name='product',
            name='width',
        ),
    ]
