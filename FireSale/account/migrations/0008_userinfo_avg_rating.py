# Generated by Django 4.0.4 on 2022-05-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_item_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='avg_rating',
            field=models.IntegerField(default=0),
        ),
    ]
