# Generated by Django 4.1.6 on 2023-04-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_auto_20210720_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='kannur', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='house',
            field=models.CharField(default='indevaram', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default='kerala', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='street',
            field=models.CharField(default='illikunnu', max_length=50),
            preserve_default=False,
        ),
    ]
