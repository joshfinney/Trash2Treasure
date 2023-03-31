# Generated by Django 4.1.5 on 2023-03-08 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("logins", "0001_initial"),
        ("event", "0001_initial"),
        ("location", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="trash",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="logins.player"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="locationId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="location.location"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="questionSet",
            field=models.ManyToManyField(to="event.question"),
        ),
        migrations.AddField(
            model_name="event",
            name="trashId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="event.trash"
            ),
        ),
    ]