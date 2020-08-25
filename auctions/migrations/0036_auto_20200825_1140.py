# Generated by Django 3.0.8 on 2020-08-25 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_auto_20200823_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='winner',
        ),
        migrations.AddField(
            model_name='auction',
            name='winner',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
