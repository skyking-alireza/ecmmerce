# Generated by Django 4.0.1 on 2022-04-10 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
        ('main', '0002_logo_site_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='navbar_process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('descriptions', models.CharField(max_length=100)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.images')),
            ],
        ),
    ]
