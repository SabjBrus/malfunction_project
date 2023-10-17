from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import PermissionsMixin

from users.generate_slug import generate_slug


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


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


class CustomUser(AbstractBaseUser, PermissionsMixin):
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
        validators=[
            RegexValidator(
                regex=(
                    r'^[A-Za-zА-Яа-я0-9~@#$%^&*()_+{}\[\]:;"<>/?!\.\'`-]{5,40}$'
                ),
                message=(
                    "Пароль должен содержать от 5 до 50 символов и может"
                    " включать буквы, цифры и специальные символы:"
                    " ~@#$%^&*()_+{}[]:;\"<>/?!.'`-"
                ),
            )
        ],
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
    slug = models.SlugField(
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
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.first_name, self.last_name)
        super().save(*args, **kwargs)
