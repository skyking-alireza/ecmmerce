# Generated by Django 4.0.1 on 2022-07-13 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_category_blog_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='viewsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
        ),
    ]