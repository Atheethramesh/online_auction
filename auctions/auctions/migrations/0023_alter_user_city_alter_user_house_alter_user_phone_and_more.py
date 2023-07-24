# Generated by Django 4.1.6 on 2023-04-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_user_city_user_house_user_phone_user_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='house',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='street',
            field=models.CharField(max_length=100),
        ),
    ]
