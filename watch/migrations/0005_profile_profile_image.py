# Generated by Django 3.1.2 on 2020-10-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0004_remove_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='/../../Logo.JPG', upload_to='profile-pics'),
        ),
    ]
