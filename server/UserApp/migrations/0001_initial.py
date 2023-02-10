# Generated by Django 4.1.6 on 2023-02-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=500)),
                ("password", models.CharField(max_length=500)),
                ("email", models.EmailField(max_length=500)),
            ],
            options={
                "db_table": "users",
            },
        ),
    ]