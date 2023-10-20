from django.db import models

from users.models import CustomUser

STATUSES = (
    ('NEW', 'new'),
    ('IN_PROGRESS', 'in progress'),
    ('DONE', 'done'),
)


class Defect(models.Model):
    title = models.CharField()
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    body = models.CharField()
    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        default='NEW',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата регистрации замечания',
        auto_now_add=True,
    )
