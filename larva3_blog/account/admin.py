from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username','firstname','lastname','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','username','firstname')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    ordering =()
    fieldsets =()

admin.site.register(Account,AccountAdmin)