from django.db import models


class Like(models.Model):

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE, related_name="likes")
    song_id = models.ForeignKey("Song", on_delete=models.CASCADE, related_name="likes")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [["user_id", "song_id"]]
