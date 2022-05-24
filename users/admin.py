from django.contrib import admin
from users.models import User #Registrar nuevo modelo de usuario
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin #Alias para que no se lie

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
    # fieldsets = (
    #     (None , {'fields' : ('username', 'password')}),
    #     ('Información Personal', {'fields': ('first_name', 'last_name','email')}),
    #     ('Redes sociales', {'fields': ('linkedin',)})
    # )
