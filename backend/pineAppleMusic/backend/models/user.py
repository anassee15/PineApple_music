from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserGender(models.TextChoices):
        MAN = "MAN", "Man"
        WOMAN = "WOMAN", "Woman"
        OTHER = "OTHER", "Other"

    gender = models.CharField(
        max_length=10, choices=UserGender.choices, default=UserGender.OTHER
    )
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True)
    description = models.TextField(blank=True)
    is_artist = models.BooleanField(default=False)

    def like_song_id(self):
        # return song who are liked by the user
        return self.likes.values_list("song_id", flat=True)
