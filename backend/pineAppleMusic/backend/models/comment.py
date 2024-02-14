from django.db import models


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="comments"
    )
    song_id = models.ForeignKey(
        "Song", on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def username(self):
        return self.user_id.username

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["id", "user_id"], name="comment_keys")
        ]
