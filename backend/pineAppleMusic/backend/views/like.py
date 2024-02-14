from rest_framework import viewsets
from rest_framework import permissions

from ..models import Like
from ..serializers import LikeSerializer

from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(tags=["Like"])
class LikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows likes to be viewed or edited.
    """

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["Like"]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            return Like.objects.filter(user_id=user_id)
        return Like.objects.all()
