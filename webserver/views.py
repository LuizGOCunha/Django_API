# importamos aqui a resposta de dados em Json
# from django.http import JsonResponse


# Essa função verifica o método do httprequest e entrega de volta dados de acordo com o que é pedido
# def data(request):
#    if request.method == 'GET':
#        dados = {'chave': 'valor',}
#        return JsonResponse(dados)

from rest_framework import viewsets
from webserver.models import Dados
from webserver.serializer import DadoSerializer

class DadosViewSet(viewsets.ModelViewSet):
    """buscando todos os objetos Dados, então selecionando a classe serializer"""
    queryset = Dados.objects.all()
    serializer_class = DadoSerializer
