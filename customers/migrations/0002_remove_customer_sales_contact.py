# Generated by Django 3.2.8 on 2021-10-06 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='sales_contact',
        ),
    ]