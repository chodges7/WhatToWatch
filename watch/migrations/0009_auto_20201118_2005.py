# Generated by Django 3.1.2 on 2020-11-18 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0008_auto_20201020_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='watch/static/LogoColor.png', null=True, upload_to='watch/static/profile-pics'),
        ),
    ]
