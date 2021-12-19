from rest_framework import serializers
from webserver.models import Dados


# Essa classe irá ler os dados presentes nos bancos de dados e retornar no formato Json como httpresponse ao client
# em models, será especificado quais modelos devem ser visualizados pelo serializer, em fields, quais os atributos.
class DadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = ['id', 'nome', 'integer', 'data', 'bool', 'binary', 'observation']