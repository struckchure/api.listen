from django.urls import path

from song.api import (
    ListCreateUpdateSongAPI,
    RetrieveDeleteSongAPI,
    ListCreateUpdateAlbumAPI,
    RetrieveDeleteAlbumAPI,
)

app_name = "song"


urlpatterns = [
    path("song/", view=ListCreateUpdateSongAPI.as_view(), name="song__list_add_update"),
    path(
        "song/<int:pk>/",
        view=RetrieveDeleteSongAPI.as_view(),
        name="song__detail_update_delete",
    ),
    path(
        "album/", view=ListCreateUpdateAlbumAPI.as_view(), name="album__list_add_update"
    ),
    path(
        "album/<int:pk>/",
        view=RetrieveDeleteAlbumAPI.as_view(),
        name="album__detail_update_delete",
    ),
]
