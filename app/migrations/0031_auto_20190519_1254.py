# Generated by Django 2.1.5 on 2019-05-19 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_userprofile_is_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSuggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('suggested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile')),
            ],
        ),
        migrations.AlterField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='app.Post'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='app.UserProfile'),
        ),
    ]
