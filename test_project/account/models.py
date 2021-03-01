from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(_('email address'), unique=True)
  username = models.CharField(max_length=255, verbose_name='username')
  role = models.CharField(max_length=255, verbose_name='role')
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  date_joined = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'role']

  objects = CustomUserManager()

  def __str___(self):
    return self.username
