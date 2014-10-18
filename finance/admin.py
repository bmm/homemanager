from django.contrib import admin
from finance.models import Entidade, Fatura, LinhaFatura, Despesa, MovimentoBancario, ContaBancaria, Receita 

class ItemDetailInline(admin.TabularInline):
    model = MovimentoBancario

#class ItemContaBancaria(admin.ModelAdmin):
#    fields = [
#        'saldo', 
#    ]

class ContaBancariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'saldo')
    fields = ('banco', 'nome', 'saldo')
    readonly_fields = ('saldo',)
    inlines = ( ItemDetailInline, )

class ItemDetailInline(admin.TabularInline):
    model = LinhaFatura

class FaturaAdmin(admin.ModelAdmin):
    list_display = ('entidade', 'data', 'valor')
    fields = ('entidade', 'data', 'valor')
    readonly_fields = ('valor',)
    inlines = ( ItemDetailInline, )

# Register your models here.
admin.site.register(Entidade)
admin.site.register(Fatura, FaturaAdmin)
#admin.site.register(LinhaFatura)
admin.site.register(Despesa)
admin.site.register(MovimentoBancario)
admin.site.register(ContaBancaria, ContaBancariaAdmin)
admin.site.register(Receita)
