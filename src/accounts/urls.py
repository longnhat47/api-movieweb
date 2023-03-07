from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('user', UserListView.as_view(), name='users'),
    path('user/login', UserLoginView.as_view(), name='login'),
    path('user/register', UserCreateView.as_view(), name='register'),
    path('user/<int:id>', UserDetailUpdateDeleteView.as_view(), name='user-detail'),
    path('user/change-password/<int:id>', UserUpdatePasswordView.as_view(), name='change-password'),
]