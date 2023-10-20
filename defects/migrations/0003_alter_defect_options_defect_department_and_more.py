# Generated by Django 4.2.6 on 2023-10-20 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0002_customuser_is_active_customuser_is_staff"),
        ("defects", "0002_alter_defect_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="defect",
            options={"verbose_name": "замечание", "verbose_name_plural": "замечания"},
        ),
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
        migrations.AlterField(
            model_name="defect",
            name="body",
            field=models.CharField(
                help_text="Опишите замечание", max_length=100, verbose_name="Замечание"
            ),
        ),
        migrations.AlterField(
            model_name="defect",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "new"),
                    ("IN_PROGRESS", "in progress"),
                    ("DONE", "done"),
                ],
                default="NEW",
                help_text="Укажите статус дефекта",
                max_length=20,
                verbose_name="Статус",
            ),
        ),
        migrations.AlterField(
            model_name="defect",
            name="title",
            field=models.CharField(
                help_text="Укажите заголовок", max_length=40, verbose_name="Заголовок"
            ),
        ),
        migrations.AlterField(
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