# Generated by Django 4.1.4 on 2023-06-07 17:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("chatapp", "0002_user_is_staff_user_password_alter_user_is_superuser"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="Password",
        ),
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.CharField(
                default=django.utils.timezone.now,
                max_length=128,
                verbose_name="password",
            ),
            preserve_default=False,
        ),
    ]
