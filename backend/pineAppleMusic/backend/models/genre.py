from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    