# Generated by Django 4.1.5 on 2023-03-08 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trash",
            name="player",
        ),
    ]
