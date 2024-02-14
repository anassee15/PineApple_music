from rest_framework import viewsets
from rest_framework import permissions

from ..models import Playlist
from ..serializers import PlaylistSerializer, SimplifiedPlaylistSerializer

from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(tags=["Playlist"])
class PlaylistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows playlists to be viewed or edited.
    """

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["Playlist"]
