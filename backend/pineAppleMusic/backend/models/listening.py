from django.db import models


class Listening(models.Model):
    user_id = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="listenings"
    )
    song_id = models.ForeignKey(
        "Song", on_delete=models.CASCADE, related_name="listenings"
    )
    last_listening_date = models.DateTimeField(auto_now_add=True)

    nb_listening = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "song_id"], name="listening_keys"
            )
        ]
