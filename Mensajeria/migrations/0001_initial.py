# Generated by Django 4.1.1 on 2022-11-04 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Mensaje",
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
                ("mensaje", models.CharField(max_length=100)),
                (
                    "destinatario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="destinatario",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "remitente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="remitente",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
