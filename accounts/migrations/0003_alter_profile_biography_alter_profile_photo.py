# Generated by Django 4.0.5 on 2022-07-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
    ]
