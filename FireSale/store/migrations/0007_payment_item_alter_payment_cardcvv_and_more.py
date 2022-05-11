# Generated by Django 4.0.4 on 2022-05-11 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_profile_bio_alter_profile_img'),
        ('store', '0006_remove_payment_amount_alter_payment_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.item'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='cardCvv',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cardNumber',
            field=models.IntegerField(),
        ),
    ]
