# Generated by Django 4.1.4 on 2023-01-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0009_playlist_genres_playlist_songs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("Man", "Man"), ("Woman", "Woman"), ("Other", "Other")],
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_artist",
            field=models.BooleanField(),
        ),
    ]