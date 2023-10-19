from django.db import models

from users.models import CustomUser


class Defect(models.Model):
    title = models.CharField()
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    body = models.CharField()
    status = models.CharField()
    created_at = models.DateTimeField(
        verbose_name='Дата регистрации замечания',
        auto_now_add=True,
    )
