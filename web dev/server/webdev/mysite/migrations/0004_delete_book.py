# Generated by Django 3.1.2 on 2020-10-07 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_remove_book_num_pages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
