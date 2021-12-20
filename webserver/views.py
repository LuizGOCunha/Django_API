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
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Em um viewset, a lógica de views relacionados podem ser unidos em uma única classe chamada ViewSet
class DadosViewSet(viewsets.ModelViewSet):
    """buscando todos os objetos Dados, então selecionando a classe serializer"""
    queryset = Dados.objects.all()
    serializer_class = DadoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

