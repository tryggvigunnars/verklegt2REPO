# Generated by Django 4.0.4 on 2022-05-10 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_bids_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('postalCode', models.FloatField()),
                ('cardNumber', models.FloatField(max_length=16)),
                ('cardMonth', models.FloatField()),
                ('cardYear', models.FloatField()),
                ('cardCvv', models.FloatField(max_length=3)),
                ('cardholderName', models.CharField(max_length=30)),
                ('amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.bids')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
