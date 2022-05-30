from django.urls import path

from account.views import LoginAPI, LogoutAPI, ProfileAPI, RegisterAPI


app_name = "account"

urlpatterns = [
    path("auth/register/", RegisterAPI.as_view(), name="register"),
    path("auth/login/", LoginAPI.as_view(), name="login"),
    path("auth/profile/", ProfileAPI.as_view(), name="profile"),
    path("auth/logout/", LogoutAPI.as_view(), name="logout"),
]
