# Generated by Django 4.2.5 on 2023-09-18 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
    ]
