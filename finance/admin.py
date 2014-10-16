from django.contrib import admin
from finance.models import Entidade, Fatura, LinhaFatura, Despesa, MovimentoBancario, ContaBancaria, Receita 

class ItemDetailInline(admin.TabularInline):
    model = MovimentoBancario

class ItemContaBancaria(admin.ModelAdmin):
    fields = [
        'saldo', 
    ]

class ContaBancariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'saldo')
    fields = ('nome', 'saldo')
    readonly_fields = ('saldo',)
    inlines = ( ItemDetailInline, )

# Register your models here.
admin.site.register(Entidade)
admin.site.register(Fatura)
admin.site.register(LinhaFatura)
admin.site.register(Despesa)
admin.site.register(MovimentoBancario)
admin.site.register(ContaBancaria, ContaBancariaAdmin)
admin.site.register(Receita)
