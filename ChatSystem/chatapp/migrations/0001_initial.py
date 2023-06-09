# Generated by Django 4.1.4 on 2023-06-07 17:45

import chatapp.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("Name", models.CharField(max_length=60)),
                ("Email", models.EmailField(max_length=254, unique=True)),
                (
                    "Password",
                    models.CharField(
                        max_length=10,
                        validators=[django.core.validators.MinLengthValidator(6)],
                    ),
                ),
                (
                    "Gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("others", "others"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "DOB",
                    models.DateField(
                        blank=True,
                        null=True,
                        validators=[chatapp.models.validate_past_date],
                    ),
                ),
                (
                    "Contact_No",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be 10 digits",
                                regex="^\\d{10}$",
                            )
                        ],
                    ),
                ),
                ("Is_available", models.BooleanField(default=False)),
                ("Created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Chat",
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
                ("message", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_chats",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_chats",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
