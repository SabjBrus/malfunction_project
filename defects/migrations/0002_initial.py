# Generated by Django 4.2.6 on 2023-10-26 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("defects", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="defect",
            name="department",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите отдел замечания",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="defect",
                to="users.department",
                verbose_name="Отдел",
            ),
        ),
        migrations.AddField(
            model_name="defect",
            name="user",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите пользователя",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="defect",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]
