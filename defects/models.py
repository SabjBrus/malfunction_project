from django.db import models

from users.models import CustomUser, Department

STATUSES = (
    ('NEW', 'new'),
    ('IN_PROGRESS', 'in progress'),
    ('DONE', 'done'),
)

PRIORITIES = (
    ('LOW', 'low'),
    ('HIGH', 'high'),
    ('MEDIUM', 'medium'),
)


class Defect(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=40,
        blank=False,
        help_text='Укажите заголовок',
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='defect',
        help_text='Укажите пользователя',
        null=True,
        blank=True,
    )
    body = models.CharField(
        verbose_name='Замечание',
        max_length=100,
        blank=False,
        help_text='Опишите замечание',
    )
    priority = models.CharField(
        verbose_name='Приоритет',
        max_length=10,
        choices=PRIORITIES,
        default='LOW',
        help_text='Укажите приоритет замечания'
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=20,
        choices=STATUSES,
        default='NEW',
        help_text='Укажите статус дефекта',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата регистрации замечания',
        auto_now_add=True,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name='Отдел',
        related_name='defect',
        help_text='Укажите отдел замечания',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'замечание'
        verbose_name_plural = 'замечания'

    def __str__(self):
        return self.title
