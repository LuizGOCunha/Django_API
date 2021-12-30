from django.contrib import admin
from webserver.models import Dados
# Register your models here.


class Admin(admin.ModelAdmin):
    # Lista as propriedades do objeto que devem ser exibidas
    list_display = ('id', 'nome', 'data')
    # Lista propriedades que devem servir de link para o objeto
    list_display_links = ('id', 'nome', 'data')
    # Cria um campo de busca que procura com base nas propriedades listadas
    search_fields = ('id', 'nome')
    # lista tantos objetos por página na página de admin
    list_per_page = 10
    # Ordena na pagina de admin com base nessas propriedades listadas
    ordering = ('nome',)


admin.site.register(Dados, Admin)