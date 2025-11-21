from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
class UserAdmin(BaseUserAdmin):
    fieldsets=(
        (None,{'fields':('username','password','is_active')}),
        ('Important dates', {'fields':('last_login','date_joined')}),
    )

    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('username','password','is_active'),
        }),
    )
    readonly_fields=('last_login','date_joined')
    list_display=('username','is_active')
    list_filter=('is_active',)
    search_fields=('username',)
    ordering=('username',)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)