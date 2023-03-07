from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from rsa import encrypt
# Create your models here.


class CustomManagerUser(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff being True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    email = models.CharField(max_length=50, null=False, unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='user_images', blank=True)
    birthday = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=True)
    username = None
    first_name= None
    last_name = None
    is_active = models.BooleanField(default=True)

    objects = CustomManagerUser()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
