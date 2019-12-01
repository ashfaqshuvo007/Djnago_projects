from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from . models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    