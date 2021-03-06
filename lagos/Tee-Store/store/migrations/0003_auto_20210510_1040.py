# Generated by Django 3.1.3 on 2021-05-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210506_2059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categorie'},
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name': 'Shipping Addres'},
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='admin@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
