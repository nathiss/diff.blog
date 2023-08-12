# Generated by Django 2.1.5 on 2021-04-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.CharField(max_length=200)),
                ("company_url", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                ("job_url", models.CharField(max_length=300)),
                ("posted_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="job",
            name="locations",
            field=models.ManyToManyField(related_name="jobs", to="jobs.Location"),
        ),
    ]
