from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from users.generate_slug import generate_slug


class Department(models.Model):
    name = models.CharField(
        verbose_name='Название отдела',
        max_length=50,
        unique=True,
        help_text='Укажите название отдела',
    )
    slug = models.SlugField(
        verbose_name='Идентификатор отдела',
        max_length=50,
        unique=True,
        help_text='Укажите идентификатор отдела',
    )

    class Meta:
        verbose_name = 'отдел'
        verbose_name_plural = 'отделы'

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=150,
        unique=True,
        blank=False,
        help_text='Укажите ваш адрес электронной почты',
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=150,
        help_text='Укажите ваш пароль',
        validators=[RegexValidator(
            regex=(
                r'^[A-Za-zА-Яа-я0-9~@#$%^&*()_+{}\[\]:;"<>/?!\.\'`-]{5,40}$'),
            message=(
                "Пароль должен содержать от 5 до 50 символов и может"
                " включать буквы, цифры и специальные символы:"
                " ~@#$%^&*()_+{}[]:;\"<>/?!.'`-")
        )
        ]
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=100,
        blank=False,
        help_text='Укажите ваше имя',
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=100,
        blank=False,
        help_text='Укажите вашу фамилию',
    )
    username = models.SlugField(
        verbose_name='Слаг',
        max_length=200,
        unique=True,
        blank=True,
    )

    date_joined = models.DateTimeField(
        verbose_name='Дата регистрации',
        auto_now_add=True,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name='Отдел',
        related_name='customuser',
        help_text='Укажите отдел пользователя',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = generate_slug(self.first_name, self.last_name)
        super().save(*args, **kwargs)
