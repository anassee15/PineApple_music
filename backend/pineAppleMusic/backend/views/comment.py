from rest_framework import viewsets
from rest_framework import permissions

from ..models import Comment
from ..serializers import CommentSerializer

from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(tags=["Comment"])
class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["Comment"]
