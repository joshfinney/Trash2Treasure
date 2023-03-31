# Generated by Django 4.1.5 on 2023-03-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0004_alter_trash_image"),
        ("logins", "0002_alter_player_bin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="bin",
            field=models.ManyToManyField(
                blank=True, related_name="players", to="event.trash"
            ),
        ),
    ]
