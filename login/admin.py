from django.contrib import admin
from . models import Usuario

@admin.register(Usuario)
class usuarioadmin(admin.ModelAdmin):
    readonly_fields = ('nome','email','senha')