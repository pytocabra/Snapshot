# Generated by Django 3.2.9 on 2021-12-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_profile.png', upload_to='profile_images'),
        ),
    ]
