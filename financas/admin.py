from django.contrib import admin

from financas.models import Transacoes

class ListandoTransacoes(admin.ModelAdmin):
    list_display = ("data_transacao", "banco_origem", "banco_destino", "valor_transacao", "id")
    list_display_links = ("id","data_transacao")
    search_fields = ("data_transacao",)
    list_filter = ("banco_origem", "banco_destino", "data_transacao")
    # list_editable = ()
    list_per_page = 10

admin.site.register(Transacoes, ListandoTransacoes)
