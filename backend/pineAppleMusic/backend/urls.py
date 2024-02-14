from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"album", views.AlbumViewSet)
router.register(r"comment", views.CommentViewSet)
router.register(r"genre", views.GenreViewSet)
router.register(r"like", views.LikeViewSet)
router.register(r"listening", views.ListeningViewSet)
router.register(r"playlist", views.PlaylistViewSet)
router.register(r"song", views.SongViewSet)
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("user/register", views.RegisterView.as_view()),
]
