from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate, login, logout

from listen.utils import View
from account.serializers import UserSerializer, UserLoginSerializer


class RegisterAPI(View):
    """
    Register API
    """

    serializer_class = UserSerializer

    def post(self, request):
        """
        Register
        """

        user_data = request.data
        user_register_serializer = self.serializer_class(data=user_data)
        user_register_serializer.is_valid(raise_exception=True)
        user_register_serializer.save()

        return Response(user_register_serializer.data, status=status.HTTP_201_CREATED)


class LoginAPI(View):
    """
    Login API
    """

    serializer_class = UserLoginSerializer

    def post(self, request):
        """
        Login
        """

        user_credentials = request.data
        user_login_serializer = self.serializer_class(data=user_credentials)
        user_login_serializer.is_valid(raise_exception=True)

        username = user_login_serializer.validated_data["username"]
        password = user_login_serializer.validated_data["password"]

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
        login(request, user)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status=status.HTTP_200_OK)


class LogoutAPI(View):
    """
    Logout API
    """

    def post(self, request):
        """
        Logout
        """

        logout(request)

        if request.user.is_authenticated:
            token = Token.objects.filter(user=request.user)

            if token.exists():
                token.delete()

        return Response(
            {"message": "You're currently logged out"}, status=status.HTTP_200_OK
        )


class ProfileAPI(View):
    """
    Profile API
    """

    serializer_class = UserSerializer
    permision_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get Profile
        """

        user_data = request.user
        user_serializer = self.serializer_class(user_data)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        """
        Update Profile
        """

        user_update_data = request.data
        user_update_serializer = self.get_serializer(
            request.user, data=user_update_data, partial=True
        )
        user_update_serializer.is_valid(raise_exception=True)
        user_update_serializer.save()

        return Response(user_update_serializer.data, status=status.HTTP_200_OK)
