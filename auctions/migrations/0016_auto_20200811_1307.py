# Generated by Django 3.1 on 2020-08-11 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20200811_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='number_watchlist',
            field=models.IntegerField(default=0),
        ),
    ]