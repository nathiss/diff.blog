# Generated by Django 2.1.5 on 2021-06-06 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_auto_20210530_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsuggestion',
            name='status',
            field=models.IntegerField(choices=[(10, 'Blog added'), (3, 'Should be added by the user'), (1, 'No GitHub account'), (4, 'Non English blog'), (0, 'Pending'), (2, 'No feed')], default=0),
        ),
    ]
