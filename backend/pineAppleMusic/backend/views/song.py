from rest_framework import viewsets
from rest_framework import permissions

from ..models import Song
from ..serializers import SongSerializer

from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(tags=["Song"])
class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows songs to be viewed or edited.
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["Song"]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            return Song.objects.filter(user_id=user_id)
        return Song.objects.all()

    # to delete the song cover and song path when the song is deleted
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.song_cover.delete()
        instance.song_path.delete()
        return super().destroy(request, *args, **kwargs)
