# Generated by Django 3.2.9 on 2021-12-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snap',
            name='tag',
            field=models.ManyToManyField(blank=True, to='main.Tag'),
        ),
    ]
