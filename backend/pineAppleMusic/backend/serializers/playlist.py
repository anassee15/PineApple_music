from rest_framework import serializers
from ..models import Playlist


class SimplifiedPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = [
            "id",
            "user_id",
            "title",
            "description",
            "playlist_cover",
            "is_private",
        ]


class PlaylistSerializer(SimplifiedPlaylistSerializer):

    from .song import SimplifiedSongSerializer
    from .genre import GenreSerializer

    songs = SimplifiedSongSerializer(many=True, read_only=True)
    genre = GenreSerializer(many=False, read_only=True)

    class Meta:
        model = Playlist
        fields = SimplifiedPlaylistSerializer.Meta.fields + ["songs", "genre"]
