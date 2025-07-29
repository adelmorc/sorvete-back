from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('src.usuarios.urls')),
    path('produtos/', include('src.produtos.urls')),
    path('fornecedores/', include('src.fornecedores.urls')),
    path('estoque/', include('src.estoque.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
