# Generated by Django 4.0.4 on 2022-05-06 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.status'),
        ),
    ]
