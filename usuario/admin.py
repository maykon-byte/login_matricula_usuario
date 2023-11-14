from django.contrib import admin
from django.db import models
from django.db.models.query_utils import select_related_descend
from . models import Pessoa,Pedido,Cargos
from django_object_actions import DjangoObjectActions
from django.http.response import HttpResponse
from django.shortcuts import render


class PedidoInline(admin.TabularInline):
    readonly_fields = ('nome','quantidade','descricao')
    list_display = ('nome','quantidade','descricao')
    model = Pedido
    extra = 0


@admin.register(Pessoa)
class Pessoaadmin(DjangoObjectActions, admin.ModelAdmin):
    inlines = [PedidoInline]
    list_display=('get_foto','nome','sobrenome','email','nome_completo')

    def matricula(self, request, pessoa):
        return render (request,'matricula.html')
    
    matricula.label= "matricula"
    change_actions=("matricula",)

admin.site.register(Pedido)
admin.site.register(Cargos)


