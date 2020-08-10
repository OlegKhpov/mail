# Generated by Django 3.0.8 on 2020-08-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200805_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('HOME', 'Home'), ('TOYS', 'Toys'), ('POTI', 'Potions'), ('BOOK', 'Books'), ('ARTI', 'Artifacts')], max_length=4),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(height_field=64, upload_to='images', width_field=64),
        ),
    ]
