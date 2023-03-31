# Generated by Django 4.1.5 on 2023-03-08 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("eventId", models.AutoField(primary_key=True, serialize=False)),
                ("status", models.CharField(max_length=100)),
                ("startDateTime", models.DateTimeField()),
                ("endDateTime", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("questionId", models.AutoField(primary_key=True, serialize=False)),
                ("question", models.CharField(max_length=100)),
                ("answer", models.CharField(max_length=100)),
                ("wrongAnswer1", models.CharField(max_length=100)),
                ("wrongAnswer2", models.CharField(max_length=100)),
                ("wrongAnswer3", models.CharField(max_length=100)),
                ("wrongAnswer4", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Trash",
            fields=[
                ("trashId", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("value", models.IntegerField()),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
    ]
