from rest_framework.serializers import ModelSerializer
from .models import User

#Login
class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

class UserLoginResponseSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'image', 'birthday', 'is_superuser']

#View List, Register
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'full_name', 'image', 'birthday', 'status']
        extra_kwargs = {
            'password': {'write_only': True},
            'status': {'read_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


#User in comment
class UserCommentSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'image']


#Update User
class UpdateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'image', 'birthday']
        extra_kwargs = {
            'email': {'read_only': True}
        }


#Update User Password
class UpdatePasswordUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }