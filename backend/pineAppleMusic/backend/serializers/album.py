from rest_framework import serializers
from ..models import Album


class SimplifiedAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            "id",
            "user_id",
            "title",
            "release_date",
            "album_cover",
        ]


class AlbumSerializer(SimplifiedAlbumSerializer):

    from .song import SimplifiedSongSerializer

    songs = SimplifiedSongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = SimplifiedAlbumSerializer.Meta.fields + ["songs"]
