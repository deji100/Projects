# Generated by Django 3.1.3 on 2021-03-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0011_auto_20210326_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sold_out',
            field=models.BooleanField(default=False),
        ),
    ]