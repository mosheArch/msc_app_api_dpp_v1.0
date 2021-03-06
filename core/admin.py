from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User
from django.utils.translation import gettext as _

from core.models.model_datosSociodemograficos import DatosSociodemograficos, resultdoPrediccion
from core.models.model_edimburgo import CuestionarioEdimburgo, resultdoEdimburgo


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(DatosSociodemograficos)
admin.site.register(resultdoPrediccion)
admin.site.register(CuestionarioEdimburgo)
admin.site.register(resultdoEdimburgo)
