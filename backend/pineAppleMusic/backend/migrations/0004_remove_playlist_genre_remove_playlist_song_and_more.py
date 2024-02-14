# Generated by Django 4.1.2 on 2022-10-19 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0003_remove_playlist_privacy_remove_song_privacy_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="playlist",
            name="genre",
        ),
        migrations.RemoveField(
            model_name="playlist",
            name="song",
        ),
        migrations.RemoveField(
            model_name="song",
            name="genre",
        ),
        migrations.CreateModel(
            name="SongGenre",
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
                (
                    "genre_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="song_genre",
                        to="backend.genre",
                    ),
                ),
                (
                    "song_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="song_genre",
                        to="backend.song",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PlaylistSong",
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
                (
                    "playlist_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="playlist_song",
                        to="backend.playlist",
                    ),
                ),
                (
                    "song_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="playlist_song",
                        to="backend.song",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PlaylistGenre",
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
                (
                    "genre_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="playlist_genre",
                        to="backend.genre",
                    ),
                ),
                (
                    "playlist_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="playlist_genre",
                        to="backend.playlist",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="songgenre",
            constraint=models.UniqueConstraint(
                fields=("id", "song_id", "genre_id"), name="song_genre_keys"
            ),
        ),
        migrations.AddConstraint(
            model_name="playlistsong",
            constraint=models.UniqueConstraint(
                fields=("playlist_id", "song_id"), name="playlist_song_keys"
            ),
        ),
        migrations.AddConstraint(
            model_name="playlistgenre",
            constraint=models.UniqueConstraint(
                fields=("playlist_id", "genre_id"), name="playlist_genre_keys"
            ),
        ),
    ]