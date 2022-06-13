from django.db import models
from rest_framework.generics import GenericAPIView
import uuid


class BaseModel(models.Model):
    """
    BaseModel
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class View(GenericAPIView):
    """
    View
    """
