from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
    # Autenticação
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # CRUD
    path('list/', views.UsuariosCreateListView.as_view(), name='usuarios_create_list'),
    path('<int:pk>/', views.UsuariosRetrieveUpdateDestroyView.as_view(), name='usuarios_detail'),
]