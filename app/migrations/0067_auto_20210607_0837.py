# Generated by Django 2.1.5 on 2021-06-07 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0066_auto_20210606_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsuggestion',
            name='status',
            field=models.IntegerField(choices=[(10, 'Blog added'), (2, 'No feed'), (3, 'Should be added by the user'), (4, 'Non English blog'), (0, 'Pending'), (1, 'No GitHub account')], default=0),
        ),
    ]
