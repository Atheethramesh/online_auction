# Generated by Django 4.1.5 on 2023-04-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0026_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='house',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
    ]