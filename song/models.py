from django.db import models

from listen.utils import BaseModel
from account.models import User


class __BaseModel(BaseModel):
    """
    BaseModel for `Album` and `Song`
    """

    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    num_stars = models.IntegerField()

    class Meta:
        abstract = True


class Album(__BaseModel):
    """
    Album
    """

    release_date = models.DateField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        return self.name


class Song(__BaseModel):
    """
    Song
    """

    album = models.ForeignKey(Album, on_delete=models.SET_NULL, default=None, null=True)

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    def __str__(self):
        return self.name
