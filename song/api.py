from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from listen.utils import View
from song.models import Album, Song
from song.serializers import AlbumSerializer, SongSerializer


class ListCreateUpdateAlbumAPI(View):
    """
    Create/Update Album API
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permision_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        """
        Get Albums
        """

        albums = self.get_queryset()
        serializer = self.get_serializer(albums, many=True)

        return Response(serializer.data)

    def post(self, request):
        """
        Create Album
        """

        album_data = request.data
        album_serializer = self.get_serializer(data=album_data)
        album_serializer.is_valid(raise_exception=True)
        album_serializer.save()

        return Response(album_serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        """
        Update Album
        """

        album = self.get_object()
        album_data = request.data
        album_serializer = self.get_serializer(album, data=album_data, partial=True)
        album_serializer.is_valid(raise_exception=True)
        album_serializer.save()

        return Response(album_serializer.data)


class RetrieveDeleteAlbumAPI(View):
    """
    Retrieve/Delete Album API
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        """
        Get Album
        """

        album = self.get_object()
        serializer = self.get_serializer(album)

        return Response(serializer.data)

    def delete(self, request, pk):
        """
        Delete Album
        """

        album = self.get_object()
        album.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ListCreateUpdateSongAPI(View):
    """
    Create/Update Song API
    """

    queryset = Song.objects.all().order_by("-created", "-updated")
    permision_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SongSerializer

    def get(self, request):
        """
        Get Songs
        """

        songs = self.get_queryset()
        serializer = self.get_serializer(songs, many=True)

        return Response(serializer.data)

    def post(self, request):
        """
        Add Song
        """

        song_data = request.data
        song_serializer = self.serializer_class(data=song_data)
        song_serializer.is_valid(raise_exception=True)
        song_serializer.save()

        return Response(song_serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        """
        Update Song
        """

        song_data = request.data
        song_serializer = self.serializer_class(data=song_data, partial=True)
        song_serializer.is_valid(raise_exception=True)
        song_serializer.save()

        return Response(song_serializer.data, status=status.HTTP_200_OK)


class RetrieveDeleteSongAPI(View):
    """
    Retrive/Delete Song API
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permision_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        """
        Get Song
        """

        song = self.get_object()
        serializer = self.get_serializer(song)

        return Response(serializer.data)

    def delete(self, request, pk):
        """
        Delete Song
        """

        song = self.get_object()
        song.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
