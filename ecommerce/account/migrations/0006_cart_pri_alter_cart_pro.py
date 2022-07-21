# Generated by Django 4.0.1 on 2022-05-09 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_variable_price_options'),
        ('account', '0005_orders_payment_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='pri',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.DO_NOTHING, to='product.variable_price'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='pro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product'),
        ),
    ]
