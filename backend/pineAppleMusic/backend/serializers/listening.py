from rest_framework import serializers
from ..models import Listening


class ListeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listening
        fields = [
            "user_id",
            "song_id",
            "last_listening_date",
            "nb_listening",
        ]
