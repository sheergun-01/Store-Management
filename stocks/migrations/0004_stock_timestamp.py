# Generated by Django 3.0.8 on 2020-07-28 11:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20200728_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]