"""listen URL Configuration
"""
from django.urls import path, include

urlpatterns = [
    path("api/v1/", include("account.urls")),
    path("api/v1/", include("song.urls")),
]
