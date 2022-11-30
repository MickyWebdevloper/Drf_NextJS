from wsgiref import validate
from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password Confirm'}
    )

    class Meta:
        model = User
        fields = ['email', 'name', 'tc', 'password', 'password2']
        # depth = 1  # for nested serializer
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        """
        Check that start is before finish.
        """
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError(
                "Password And Password Confermatin not matched !!!")
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    # def validate(self, data):
    #     """
    #     Validating email and password provided from FronTent
    #     """
    #     email = data.get('email', None)
    #     password = data.get('password', None)

    #     return None
