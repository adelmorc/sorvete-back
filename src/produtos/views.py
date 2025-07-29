from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Produto
from .serializers import ProdutoSerializer
from ..basico.funcoes import formatar_moeda


# Generic View CREATE and LIST
class ProdutoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        produtos = []

        for produto in queryset:
            produtos.append({
                'id': produto.id,
                'nome': produto.nome,
                'valor_compra': formatar_moeda(produto.valor_compra),
                'valor_venda': formatar_moeda(produto.valor_venda),
                'unidade': formatar_moeda(produto.unidade),
                'data_cadastro': produto.data_cadastro.strftime('%d/%m/%Y') if produto.data_cadastro else None,
                'imagem': produto.imagem.url,
            })

        return Response(produtos)



# Generic View UPDATE, DETAIL and DELETE
class ProdutoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
