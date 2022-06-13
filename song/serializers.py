from rest_framework import serializers

from song.models import Album, Song


class AlbumSerializer(serializers.ModelSerializer):
    """
    Album Serializer
    """

    class Meta:
        model = Album
        fields = "__all__"
        read_only_fields = ("id",)


class SongSerializer(serializers.ModelSerializer):
    """
    Song Serializer
    """

    class Meta:
        model = Song
        fields = "__all__"
        read_only_fields = ("id",)
