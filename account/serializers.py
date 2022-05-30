from rest_framework import serializers

from account.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer
    """

    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "avatar", "bio", "password")
        read_only_fields = ("id",)

    def create(self, validated_data):
        """
        Create
        """

        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user


class UserLoginSerializer(serializers.Serializer):
    """
    User Login Serializer
    """

    username = serializers.CharField()
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
