# Generated by Django 2.1.5 on 2021-05-30 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20210530_1056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='url',
            new_name='description_link',
        ),
    ]
