from rest_framework import viewsets
from rest_framework import permissions

from ..models import Album
from ..serializers import AlbumSerializer, SimplifiedAlbumSerializer

from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(tags=["Album"])
class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows albums to be viewed or edited.
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["Album"]
