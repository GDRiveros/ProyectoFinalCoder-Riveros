# Generated by Django 4.1.1 on 2022-10-30 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("BlogCoder", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="autor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="BlogCoder.autor"
            ),
        ),
    ]