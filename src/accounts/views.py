from django.contrib.auth import authenticate, get_user_model

from rest_framework.generics import (
    ListAPIView, 
    RetrieveUpdateDestroyAPIView,
    RetrieveDestroyAPIView, 
    CreateAPIView,
    UpdateAPIView)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import User
from .serializers import *
from .tokens import create_jwt

# Create your views here.
class UserLoginView(CreateAPIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = create_jwt(user)
            user = get_user_model().objects.filter(email=email)
            u = UserLoginResponseSerializer(instance=user, many = True).data
            response = {"user": u[0],"token": token}
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data={"message":"Login fail"}, status=status.HTTP_400_BAD_REQUEST)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]



class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated]

    lookup_field = 'id'

class UserUpdatePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdatePasswordUserSerializer

    lookup_field = 'id'