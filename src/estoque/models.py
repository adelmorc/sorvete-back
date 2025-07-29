from django.db import models

TIPO = (
    ('S', 'SAIDA'),
    ('E', 'ENTRADA')
)

class EstoqueEntrada(models.Model):

    produto = models.ForeignKey('produtos.Produto', on_delete=models.PROTECT, related_name='entrada_produto')
    fornecedor = models.ForeignKey('fornecedores.Fornecedor', on_delete=models.PROTECT, related_name='entrada_fornecedor')
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    fabricacao = models.DateField()
    validade = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=1, choices=TIPO, default='E', editable=False)

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade}'


class EstoqueSaida(models.Model):

    produto = models.ForeignKey('produtos.Produto', on_delete=models.PROTECT, related_name='saida_produto')
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    destino = models.CharField(max_length=200)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=1, choices=TIPO, default='S', editable=False)


    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade}'

