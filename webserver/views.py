# importamos aqui a resposta de dados em Json
# from django.http import JsonResponse


# Essa função verifica o método do httprequest e entrega de volta dados de acordo com o que é pedido
# def data(request):
#    if request.method == 'GET':
#        dados = {'chave': 'valor',}
#        return JsonResponse(dados)

from rest_framework import viewsets, filters
from webserver.models import Dados
from webserver.serializer import DadoSerializer, DadoSerializerV2
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend


# Em um viewset, a lógica de views relacionados podem ser unidos em uma única classe chamada ViewSet
class DadosViewSet(viewsets.ModelViewSet):
    """buscando todos os objetos Dados, então selecionando a classe serializer"""
    queryset = Dados.objects.all()
    serializer_class = DadoSerializer
    # authentication_classes:
    # BasicAuthentication: Uma classe com o fim de criar autenticação básica
    # permission_classes:
    # IsAuthenticated: Uma classe para manter e checar se o usuario está logado
    # DjangoModelPermissions: Importa as permissões mantidas no console do admin do django para a API
    # Todos esses acima podem ser passados como padrão na configuração do Django, e por isso foram removidos


    # Esse campo é responsável por passar a mesma orndenação que temos na nossa pagina de admin para a pagina REST_API
    # Primeiro importamos a propriedade do DjangoFilterBackend, e especificamos que utilizaremos um filtro de ordenação
    # Logo abaixo especificamos a propriedade com base em qual devemos ordenar os objetos.
    # Estas propriedades estarão disponíveis para ordenação em uma caixa de dialogo chamada "Filters"
    # Além disso também disponibilizamos um campo de busca parecido com o que temos no admin, em SearchField
    # Depois especificamos as propriedades a serem buscadas.
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'nome', 'integer']
    search_fields = ['id', 'nome', 'integer']
    # Abaixo listamos um valor booleano que podemos filtrar todos os itens marcados "True" e "False"
    filterset_fields = ['bool',]
    # Abaixo podemos especificar quais os metodos http permitidos para esse ViewSet
    http_method_names = ['get', 'put', 'patch', 'post', 'delete']

    # Abaixo temos o método que será chamado para saber qual versão deve ser usada com base nos parametros passados
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return DadoSerializerV2
        else:
            return DadoSerializer



















