from django.db import models


class AlbumSong(models.Model):
    album_id = models.ForeignKey(
        "Album", on_delete=models.CASCADE, related_name="songs"
    )
    song_id = models.ForeignKey("Song", on_delete=models.CASCADE, related_name="albums")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["album_id", "song_id"], name="album_song_keys"
            )
        ]
