from django.db import models


class PlaylistGenre(models.Model):
    playlist_id = models.ForeignKey(
        "Playlist", on_delete=models.CASCADE, related_name="playlist_genre"
    )
    genre_id = models.ForeignKey(
        "Genre", on_delete=models.CASCADE, related_name="playlist_genre"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["playlist_id", "genre_id"], name="playlist_genre_keys"
            )
        ]
