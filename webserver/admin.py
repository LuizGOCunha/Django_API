from django.contrib import admin
from webserver.models import Dados
# Register your models here.


class Admin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data')
    list_display_links = ('id', 'nome', 'data')
    search_fields = ('id', 'nome')
    list_per_page = 30


admin.site.register(Dados, Admin)