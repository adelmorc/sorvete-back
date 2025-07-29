from django.contrib import admin
from src.produtos.models import Produto, Categoria

admin.site.register(Produto)
admin.site.register(Categoria)