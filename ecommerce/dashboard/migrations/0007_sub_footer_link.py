# Generated by Django 4.0.1 on 2022-04-04 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_sub_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_footer',
            name='link',
            field=models.CharField(default='google.com', max_length=450),
            preserve_default=False,
        ),
    ]