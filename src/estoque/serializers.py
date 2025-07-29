from rest_framework import serializers
from .models import EstoqueEntrada, EstoqueSaida
from ..produtos.serializers import ProdutoSerializer
from ..fornecedores.serializers import FornecedorSerializer


class EntradaSerializerList(serializers.ModelSerializer):
    produto = ProdutoSerializer()
    fornecedor = FornecedorSerializer()

    class Meta:
        model = EstoqueEntrada
        fields = '__all__'


class SaidaSerializerList(serializers.ModelSerializer):
    produto = ProdutoSerializer()

    class Meta:
        model = EstoqueSaida
        fields = '__all__'


class EntradaSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstoqueEntrada
        fields = '__all__'


class SaidaSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstoqueSaida
        fields = '__all__'
