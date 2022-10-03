# Generated by Django 4.1.1 on 2022-10-03 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_auto_20221002_2241"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="status",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="posts.status",
            ),
        ),
    ]
