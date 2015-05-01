from django.contrib import admin
from core.models import Moto, Cliente, Funcionario, Venda, Peca, Abastecedor, Item

class ItemInline(admin.TabularInline):
	model = Item

class MotoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano')
    search_fields = ['marca', 'modelo', 'placa']
    list_filter =  ['marca', 'modelo', 'placa']


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'moto')


class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cpf')

class VendaAdmin(admin.ModelAdmin):
	list_display = ['cliente','funcionario', 'valor_total', 'data']
	inlines = [ItemInline]

class PecaAdmin(admin.ModelAdmin):
	list_display = ('nome','marca','preco','disponibilidade','quantidade')

class AbastecedorAdmin(admin.ModelAdmin):
	list_display = ('nome', 'peca')

admin.site.register(Moto, MotoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Peca, PecaAdmin)
admin.site.register(Abastecedor, AbastecedorAdmin)