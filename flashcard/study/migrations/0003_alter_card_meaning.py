# Generated by Django 4.1 on 2023-04-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("study", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="meaning",
            field=models.CharField(max_length=200),
        ),
    ]