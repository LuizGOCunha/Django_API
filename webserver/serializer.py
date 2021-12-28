from rest_framework import serializers
from webserver.models import Dados
from webserver.validators import *
import re


# Essa classe irá ler os dados presentes nos bancos de dados e retornar no formato Json como httpresponse ao client
# Permite que dados complexos como querysets e models sejam convertidos a python, onde podem ser renderizados como Json.
# em models, será especificado quais modelos devem ser visualizados pelo serializer, em fields, quais os atributos.
class DadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = ['id', 'nome', 'integer', 'data', 'bool', 'binary', 'observation']
# O nome da vunção de validação DEVE TER O NOME 'validate' SEGUIDO PELO ATRIBUTO. Ou não irá reconhecer.
    def validate_nome(self, nome):
        caracteres_proibidos = re.compile('[@_!#$%^&*()<>?/|\\\}{~\[\]:0123456789]')
        nome_valido = caracteres_proibidos.search(nome) is None
        if nome_valido:
            return nome
        if not nome_valido:
            raise serializers.ValidationError('O nome não deve conter símbolos ou números')

    # Mas também é possível fazer um validate de vários campos (É até recomendável)
    # Aqui ele tá checando o boolean dessas funções, que validam nossos campos
    # Então erguendo um validationError quando é necessário, retornando em um dict que faz referencia ao campo
    # Se você não retornar um dict que faz referencia ao campo, ele ergue o erro, mas retorna com non_field_error
    def validate(self, data):
        if not integer_valida(data['integer']):
            raise serializers.ValidationError({'integer': 'integer não pode ser maior que 500'})
        if not data_valida(data['data']):
            raise serializers.ValidationError({'data': 'O ano não pode ser maior que 2500'})
        if nono_catcher(data['observation']):
            raise serializers.ValidationError({'observation': 'Come on now! No cussing >:('})
        else:
            return data
