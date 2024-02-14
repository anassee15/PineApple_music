from rest_framework import viewsets
from rest_framework import permissions

from ..models import Genre
from ..serializers import GenreSerializer

from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(tags=["Genre"])
class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows genres to be viewed or edited.
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["Genre"]
