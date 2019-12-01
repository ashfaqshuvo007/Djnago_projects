from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

# User manager instance for our Customer User model
class CustomUserManager(UserManager):
    pass

#User Model
class CustomUser(AbstractUser):
    objects = CustomUserManager() 
