# Generated by Django 4.0.1 on 2022-07-04 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_variable_price_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={},
        ),
        migrations.RemoveField(
            model_name='menu',
            name='index',
        ),
    ]