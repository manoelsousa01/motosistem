from django.contrib import admin
from core.models import Moto, Cliente

class MotoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano')
    search_fields = ['marca', 'modelo', 'placa']
    list_filter =  ['marca', 'modelo', 'placa']


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'moto')

admin.site.register(Moto, MotoAdmin)
admin.site.register(Cliente, ClienteAdmin)