from rest_framework import viewsets
from rest_framework import permissions

from ..models import Listening
from ..serializers import ListeningSerializer

from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(tags=["Listening"])
class ListeningViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows listening to be viewed or edited.
    """

    queryset = Listening.objects.all()
    serializer_class = ListeningSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["Listening"]
