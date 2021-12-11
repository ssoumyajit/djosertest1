from djoser.serializers import TokenSerializer, UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class NewUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "username", "password")
        # extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
    
    def create(self, validated_data):
        """
        create a new user with encrypted password and return it
        basically overwrites the create function provided by base user class \
        and uses our custom user model
        """
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        """
        update a user, setting the password correctly and return it.
        """
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user

class NewTokenSerializer(TokenSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ("id", "email", "username")


