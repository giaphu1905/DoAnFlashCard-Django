# Generated by Django 4.1 on 2023-04-05 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("study", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="flashcard",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="card",
            name="flash_card",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="study.flashcard"
            ),
        ),
    ]
