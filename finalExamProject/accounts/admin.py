from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model


UserModel = get_user_model()


@admin.register(UserModel)
class MainUserAdmin(auth_admin.UserAdmin):
    list_display = ['username', 'is_staff', 'is_superuser','email', 'date_joined']
    list_filter = ('last_login', 'username',)
    ordering = ('-is_superuser',)
    search_fields = ('username',)
    readonly_fields = ('date_joined',)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("email", )}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", )}),
    )