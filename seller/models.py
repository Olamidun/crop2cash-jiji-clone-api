from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.conf import settings

# Create your models here.

class SellerManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, state_of_residence, password=None):
        if first_name is None:
            raise TypeError("Seller must have first name")
        if last_name is None:
            raise TypeError("Seller must have last name")
        if email is None:
            raise TypeError('Seller must supply email')

        if state_of_residence is None:
            raise TypeError('Seller must supply state of residence')
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            state_of_residence = state_of_residence,
            email = self.normalize_email(email)  
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, state_of_residence, password):
        user = self.create_user(first_name, last_name, email, state_of_residence, password)

        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_verified = True
        user.save(using=self._db)
        return user


class Seller(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300, unique = True)
    state_of_residence = models.CharField(max_length=50)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'state_of_residence']

    objects = SellerManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
