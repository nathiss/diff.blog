# Generated by Django 2.1.5 on 2021-06-07 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20210606_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='job',
            name='source',
            field=models.IntegerField(null=True),
        ),
    ]
