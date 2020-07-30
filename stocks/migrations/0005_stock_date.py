# Generated by Django 3.0.8 on 2020-07-28 12:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_stock_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]