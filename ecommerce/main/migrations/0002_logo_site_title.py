# Generated by Django 4.0.1 on 2022-04-06 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo_site',
            name='title',
            field=models.CharField(default='فروشگاه اینترنتی اسکای', max_length=150),
            preserve_default=False,
        ),
    ]