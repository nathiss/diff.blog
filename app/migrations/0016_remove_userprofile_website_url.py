# Generated by Django 2.1.5 on 2019-03-21 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_userprofile_website_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='website_url',
        ),
    ]
