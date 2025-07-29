from django.urls import path
from src.estoque import views

urlpatterns = [
    path('list/', views.EntradaSaidaListView.as_view()),
    path('entrada/', views.EntradaCreateView.as_view()),
    path('entrada/<int:id>/', views.EntradaRetrieveUpdateDestroyView.as_view()),
    path('saida/', views.SaidaCreateView.as_view()),
    path('saida/<int:id>/', views.SaidaRetrieveUpdateDestroyView.as_view()),
]
