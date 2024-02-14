from rest_framework import serializers
from ..models import Song


class SimplifiedSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            "id",
            "user_id",
            "genre",
            "title",
            "release_date",
            "song_cover",
            "song_path",
            "lyrics",
            "is_private",
        ]


class SongSerializer(SimplifiedSongSerializer):
    from .comment import CommentSerializer
    from .like import LikeSerializer

    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        fields = SimplifiedSongSerializer.Meta.fields + [
            "comments",
            "likes",
            "nb_listening",
            "nb_comments",
            "nb_likes",
        ]
