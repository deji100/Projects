# Generated by Django 3.1.3 on 2021-03-23 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0007_bid_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctioneer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='bidder',
            name='name',
        ),
        migrations.AddField(
            model_name='auctioneer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bidder',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]