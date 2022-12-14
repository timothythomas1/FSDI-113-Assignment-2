# Generated by Django 4.1.1 on 2022-10-03 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_archived_post_archived"),
    ]

    operations = [
        migrations.CreateModel(
            name="Published",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("description", models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="published",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="posts.published",
            ),
        ),
    ]
