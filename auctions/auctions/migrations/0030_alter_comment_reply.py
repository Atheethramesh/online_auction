# Generated by Django 4.1.5 on 2023-04-05 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0029_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.TextField(null=True),
        ),
    ]
