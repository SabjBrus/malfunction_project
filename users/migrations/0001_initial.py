# Generated by Django 4.2.6 on 2023-10-25 11:36

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
            name="Department",
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
                    "name",
                    models.CharField(
                        help_text="Укажите название отдела",
                        max_length=50,
                        unique=True,
                        verbose_name="Название отдела",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Укажите идентификатор отдела",
                        unique=True,
                        verbose_name="Идентификатор отдела",
                    ),
                ),
            ],
            options={
                "verbose_name": "отдел",
                "verbose_name_plural": "отделы",
            },
        ),
        migrations.CreateModel(
            name="CustomUser",
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
                (
                    "email",
                    models.EmailField(
                        help_text="Укажите ваш адрес электронной почты",
                        max_length=150,
                        unique=True,
                        verbose_name="Адрес электронной почты",
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        help_text="Укажите ваш пароль",
                        max_length=150,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Пароль должен содержать от 5 до 50 символов и может включать буквы, цифры и специальные символы: ~@#$%^&*()_+{}[]:;\"<>/?!.'`-",
                                regex="^[A-Za-zА-Яа-я0-9~@#$%^&*()_+{}\\[\\]:;\"<>/?!\\.\\'`-]{5,40}$",
                            )
                        ],
                        verbose_name="Пароль",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        help_text="Укажите ваше имя", max_length=100, verbose_name="Имя"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Укажите вашу фамилию",
                        max_length=100,
                        verbose_name="Фамилия",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=200, unique=True, verbose_name="Слаг"
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата регистрации"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите отдел пользователя",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customuser",
                        to="users.department",
                        verbose_name="Отдел",
                    ),
                ),
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
                "verbose_name": "пользователь",
                "verbose_name_plural": "пользователи",
            },
        ),
    ]
