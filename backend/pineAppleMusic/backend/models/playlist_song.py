from django.db import models


class PlaylistSong(models.Model):
    playlist_id = models.ForeignKey(
        "Playlist", on_delete=models.CASCADE, related_name="playlist_song"
    )
    song_id = models.ForeignKey(
        "Song", on_delete=models.CASCADE, related_name="playlist_song"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["playlist_id", "song_id"], name="playlist_song_keys"
            )
        ]
