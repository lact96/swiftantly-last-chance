from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    ordering = ('email',)
    search_fields = ('email',)
    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional Information', {'fields': ('company_name', 'company_address', 'is_email_user', 'domain')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
admin.site.register(Workspace)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(VirtualDomain)
admin.site.register(EmailUser)