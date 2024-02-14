from django.db import models


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE, related_name="songs")
    genre = models.ManyToManyField("Genre", related_name="songs")
    title = models.CharField(max_length=255)
    release_date = models.DateField(auto_now_add=True)
    song_cover = models.ImageField(upload_to="song_covers/", blank=True)
    song_path = models.FileField(upload_to="songs/")
    lyrics = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)

    def nb_listening(self):
        return self.listenings.aggregate(models.Sum("nb_listening"))[
            "nb_listening__sum"
        ]

    def nb_comments(self):
        return self.comments.count()

    def nb_likes(self):
        return self.likes.count()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["id", "user_id"], name="song_keys")
        ]
