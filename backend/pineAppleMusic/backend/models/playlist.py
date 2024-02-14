from django.db import models


class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="playlists"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    playlist_cover = models.ImageField(upload_to="playlist_covers/", blank=True)
    is_private = models.BooleanField(default=False)

    # associative table set manually through PlaylistSong model
    songs = models.ManyToManyField(
        "Song", related_name="playlists", through="PlaylistSong"
    )

    # associative table set manually through PlaylistGenre model
    genres = models.ManyToManyField(
        "Genre", related_name="playlists", through="PlaylistGenre"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["id", "user_id"], name="playlist_keys")
        ]
