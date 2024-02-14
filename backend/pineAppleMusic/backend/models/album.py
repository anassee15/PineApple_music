from django.db import models


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE, related_name="albums")
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    album_cover = models.ImageField(upload_to="album_covers/", blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["id", "user_id"], name="album_keys")
        ]
