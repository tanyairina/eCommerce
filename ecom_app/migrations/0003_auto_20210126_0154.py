# Generated by Django 3.1.5 on 2021-01-26 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0002_delete_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
