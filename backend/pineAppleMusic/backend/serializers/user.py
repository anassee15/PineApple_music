from rest_framework import serializers
from ..models import User

# Register
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "gender",
            "profile_picture",
            "description",
            "is_artist",
        ]


class UserSerializerComplete(UserSerializer):
    from .comment import CommentSerializer
    from .song import SimplifiedSongSerializer
    from .listening import ListeningSerializer

    comments = CommentSerializer(many=True, read_only=True)
    listenings = ListeningSerializer(many=True, read_only=True)
    songs = SimplifiedSongSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + [
            "comments",
            "songs",
            "like_song_id",
            "listenings",
        ]


# Source: https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    gender = serializers.CharField(required=True)

    is_artist = serializers.BooleanField(required=True)

    profile_picture = serializers.ImageField(required=False)

    description = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "password",
            "password2",
            "gender",
            "is_artist",
            "profile_picture",
            "description",
        )
        extra_kwargs = {
            "gender": {"required": True},
            "is_artist": {"required": True},
            "profile_picture": {"required": False},
            "description": {"required": False},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            gender=validated_data["gender"],
            is_artist=validated_data["is_artist"],
            profile_picture=validated_data["profile_picture"],
            description=validated_data["description"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
