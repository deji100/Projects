# Generated by Django 3.1.3 on 2021-05-14 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210514_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='custormer',
            new_name='customer',
        ),
    ]
