# Generated by Django 4.0.4 on 2022-05-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='dob',
            field=models.DateField(),
        ),
    ]
