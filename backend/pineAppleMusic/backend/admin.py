from django.contrib import admin
from .models import (
    Song,
    Album,
    Genre,
    Playlist,
    Like,
    User,
    Comment,
    Listening,
    PlaylistSong,
    PlaylistGenre,
    AlbumSong,
)

# Register your models here.

admin.site.register(User)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(AlbumSong)
admin.site.register(Genre)
admin.site.register(Playlist)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Listening)
admin.site.register(PlaylistSong)
admin.site.register(PlaylistGenre)
