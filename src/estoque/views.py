from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import EstoqueEntrada, EstoqueSaida
from .serializers import EntradaSerializer, SaidaSerializer, EntradaSerializerList, SaidaSerializerList


class EntradaSaidaListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        entradas = list(EstoqueEntrada.objects.all().order_by('-data_cadastro'))
        saidas = list(EstoqueSaida.objects.all().order_by('-data_cadastro'))

        registros = sorted(entradas + saidas, key=lambda obj: obj.data_cadastro, reverse=True)

        def get_serializer(obj):
            if isinstance(obj, EstoqueEntrada):
                return EntradaSerializerList(obj).data
            return SaidaSerializerList(obj).data

        return Response([get_serializer(obj) for obj in registros])


class EntradaCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = EstoqueEntrada.objects.all()
    serializer_class = EntradaSerializer


class EntradaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = EstoqueEntrada.objects.all()
    serializer_class = EntradaSerializer


class SaidaCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = EstoqueSaida.objects.all()
    serializer_class = SaidaSerializer


class SaidaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = EstoqueSaida.objects.all()
    serializer_class = SaidaSerializer
