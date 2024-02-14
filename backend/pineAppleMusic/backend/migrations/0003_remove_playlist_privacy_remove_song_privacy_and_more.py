# Generated by Django 4.1.2 on 2022-10-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0002_genre_privacy_remove_song_genre_playlist_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="playlist",
            name="privacy",
        ),
        migrations.RemoveField(
            model_name="song",
            name="privacy",
        ),
        migrations.AddField(
            model_name="playlist",
            name="is_private",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="playlist",
            name="song",
            field=models.ManyToManyField(
                related_name="playlists_song", to="backend.song"
            ),
        ),
        migrations.AddField(
            model_name="song",
            name="is_private",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.DeleteModel(
            name="Privacy",
        ),
    ]
