# Generated by Django 5.0.1 on 2024-01-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[("user", "user"), ("superuser", "superuser")], default="user", max_length=20
            ),
        ),
    ]
