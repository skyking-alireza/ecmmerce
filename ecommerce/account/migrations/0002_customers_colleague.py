# Generated by Django 4.0.1 on 2022-02-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='colleague',
            field=models.BooleanField(default=False),
        ),
    ]