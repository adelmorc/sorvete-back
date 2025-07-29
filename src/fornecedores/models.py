from django.db import models

class Fornecedor(models.Model):

    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=11)
    email_pessoal = models.EmailField(max_length=250, blank=True, null=True)
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=200, blank=True, null=True)
    uf = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(auto_now_add=True)

