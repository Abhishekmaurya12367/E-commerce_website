from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Accounts


class AccountAdmin(UserAdmin):
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'joind_time',
        'login_last',
        'is_active',
    )

    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('joind_time', 'login_last')
    ordering = ('-joind_time',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Accounts, AccountAdmin)
