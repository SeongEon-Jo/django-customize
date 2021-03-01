from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserChangeForm):

  class Meta(UserCreationForm):
    model = CustomUser
    fields = ('email', 'username', 'role')

class CustomUserChangeForm(UserChangeForm):

  class Meta:
    model = CustomUser
    fields = ('email', 'username', 'role')
