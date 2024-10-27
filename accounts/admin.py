from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm,  CustomuUserChangeForm

class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomuUserChangeForm
    model = CustomUser
    list_display = [
        'username',
        'email',
        'userid',
        'age',
        'is_staff'
    ]

    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                ('userid','age')
            ),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": (
                ('userid','age')
            ),
        }),
    )
admin.site.register(CustomUser,CustomAdmin )
    

