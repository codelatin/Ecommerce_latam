from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Auth


class AuthAdmin(UserAdmin):
    # Campos que se mostrarán en la lista del admin pilass
    list_display = ('email', 'username', 'name', 'lastname', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_active')
    
    # Campos por los que se puede buscar devs ojo
    search_fields = ('email', 'username', 'name', 'lastname')
    
    # Campos de solo lectura devs ojo
    readonly_fields = ('date_joined', 'last_login')
    
    # Filtros laterales
    list_filter = ('is_admin', 'is_staff', 'is_active', 'date_joined')
    
    # Ordenamiento por defecto ojito
    ordering = ('-date_joined',)
    
    # Configuración de los campos en el formulario de edición
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Información personal', {'fields': ('name', 'lastname', 'phone_number')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superadmin', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Configuración para el formulario de creación de usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'lastname', 'username', 'email', 'phone_number', 'password1', 'password2', 'is_active', 'is_staff', 'is_admin', 'is_superadmin'),
        }),
    )

    # Especificar que el campo de identificación es 'email'
    filter_horizontal = ('groups', 'user_permissions')
    list_display_links = ('email', 'username')


# Registrar el modelo personalizado en el admin
admin.site.register(Auth, AuthAdmin)