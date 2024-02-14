from django.contrib.auth import login
from ..models import User

from rest_framework import viewsets, permissions, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView

from ..serializers import UserSerializer, UserSerializerComplete, RegisterSerializer

from drf_yasg.utils import swagger_auto_schema


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializerComplete
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["User"]

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        if username is not None:
            # filter the queryset by the username
            self.queryset = self.queryset.filter(username=username)
        return self.queryset

    # to delete the profile picture when the user is deleted
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.profile_picture.delete()
        return super().destroy(request, *args, **kwargs)


class LoginView(KnoxLoginView):
    """
    API endpoint allowing the user to login and receive a token
    """

    permission_classes = [
        permissions.AllowAny,
    ]

    @swagger_auto_schema(request_body=AuthTokenSerializer)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginView, self).post(request, format=None)


@swagger_auto_schema(request_body=RegisterSerializer)
class RegisterView(generics.CreateAPIView):
    """
    API endpoint allowing the user to register
    """

    permission_classes = [
        permissions.AllowAny,
    ]

    serializer_class = RegisterSerializer
    swagger_tag = ["User"]
