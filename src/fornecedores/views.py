from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Fornecedor
from .serializers import FornecedorSerializer
from ..basico.funcoes import formatar_telefone, formatar_cpf_cnpj


# Generic View CREATE and LIST
class FornecedorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        fornecedores = []

        for fornecedor in queryset:
            fornecedores.append({
                'id': fornecedor.id,
                'nome': fornecedor.nome,
                'cnpj': formatar_cpf_cnpj(fornecedor.cnpj),
                'email_pessoal': fornecedor.email_pessoal,
                'telefone': formatar_telefone(fornecedor.telefone),

            })

        return Response(fornecedores)



# Generic View UPDATE, DETAIL and DELETE
class FornecedorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


