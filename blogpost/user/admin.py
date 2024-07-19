from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models  import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'timestamp', 'is_admin', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'timestamp')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, CustomUserAdmin)    
