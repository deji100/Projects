# Generated by Django 3.1.2 on 2020-10-07 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20201007_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='num_pages',
        ),
    ]