from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model =CustomUser
  list_display = ('email', 'username', 'role', 'is_staff', 'is_active')
  list_filter = ('email', 'username', 'role', 'is_staff', 'is_active')
  fieldsets = (
    (None, {'fields' : ('email', 'username', 'role')}),
    ('Permissions', {'fields' : ('is_staff', 'is_active')})
  )
  add_fieldsets = (
    (None, {
      'classes' : ('wide',),
      'fields' : ('email', 'username', 'role', 'password1', 'password2',)
    }),
  )
  search_fields = ('email',)
  ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)